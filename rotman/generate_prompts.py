import os
import csv
import json
import time
from textwrap import dedent

import openai
import hashlib
import tiktoken
import requests


DATA_DIR = os.path.join(os.path.dirname(__file__), '.data')
CACHE_DIR = os.path.join(DATA_DIR, 'cache')
os.makedirs(CACHE_DIR, exist_ok=True)


def get_from_cache(key):
    key_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
    cache_file = os.path.join(CACHE_DIR, key_hash)
    if os.path.exists(cache_file):
        with open(cache_file) as f:
            return f.read()
    return None


def set_to_cache(key, value):
    key_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
    cache_file = os.path.join(CACHE_DIR, key_hash)
    with open(cache_file, 'w') as f:
        f.write(value)


# https://redash.hasadna.org.il/queries/1272
MEETING_IDS = [
    2199806,
    2200828,
    2200179,
    2200825,
    2198385,
    2200777,
    2200180,
    2199808,
    2199179,
    2200181
]

# https://redash.hasadna.org.il/queries/1274#1456
FIRST_NAME = 'שמחה'
LAST_NAME = 'רוטמן'
ALTNAMES = ["שמחה רוטמן"]

PROMPT_GENERATION_TEXT = dedent('''
Write a prompt for a large language model such as GPT-4 to allow it to imitate the way a person speaks.
The prompt should be in English, keeping texts short but not missing important details.
The prompt should contain as much details as possible to allow the chatbot to duplicate the style of the given example text.
The response should include bullet points directing the LLM how to imitate the style and common phrases / words.
Don't preface the output with description or explanation, only write the bullet points as described.

Example text:
''')

PROMPT_AGGREGATION_TEXT = dedent('''
Write a prompt for a large language model such as GPT-4 to allow it to imitate the way a person speaks.
The prompt should be in English, keeping texts short but not missing important details.
The prompt should contain as much details as possible to allow the chatbot to duplicate the style of the given example text.
The response should include bullet points directing the LLM how to imitate the style and common phrases / words.
Don't preface the output with description or explanation, only write the bullet points as described.

Aggregate the following bullet points into a single prompt:
''')


def is_matching_header(header):
    if FIRST_NAME in header and LAST_NAME in header:
        return True
    for altname in ALTNAMES:
        if altname in header:
            return True
    return False


def get_meeting_parts_csv_url(meeting_id):
    id = str(meeting_id)
    return f'https://production.oknesset.org/pipelines/data/committees/meeting_protocols_parts/files/{id[0]}/{id[1]}/{id}.csv'


def iterate_speech_parts():
    for meeting_id in MEETING_IDS:
        print(f'Iterating speech parts for meeting {meeting_id}...')
        url = get_meeting_parts_csv_url(meeting_id)
        data = get_from_cache(url)
        if data is None:
            data = []
            csv_reader = csv.DictReader(requests.get(url).content.decode('utf-8').splitlines(), delimiter=',')
            for row in csv_reader:
                if is_matching_header(row['header']) and len(row['body']) > 100:
                    yield row['body']
                    data.append(row['body'])
            set_to_cache(url, json.dumps(data))
        else:
            for part in json.loads(data):
                yield part


def prompt_data_aggregator(initial_prompt, parts_iterator, tiktoken_enc, max_prompt_length):
    prompt = initial_prompt
    num_parts_in_prompt = 0
    for part in parts_iterator:
        new_prompt = prompt + '\n' + part
        if len(tiktoken_enc.encode(new_prompt)) > max_prompt_length:
            yield prompt
            prompt = initial_prompt + '\n' + part
            num_parts_in_prompt = 1
            assert len(tiktoken_enc.encode(prompt)) < max_prompt_length
        else:
            prompt = new_prompt
            num_parts_in_prompt += 1
    if num_parts_in_prompt > 0:
        yield prompt


def iterate_prompts(tiktoken_enc, max_prompt_length):
    yield from prompt_data_aggregator(PROMPT_AGGREGATION_TEXT, iterate_speech_parts(), tiktoken_enc, max_prompt_length)


def iterate_prompt_responses(tiktoken_enc, max_prompt_length, verbose=False, no_cache=False):
    for prompt in iterate_prompts(tiktoken_enc, max_prompt_length):
        data = get_from_cache(prompt) if not no_cache else None
        if data is None:
            print(f'Generating response for prompt of length {len(tiktoken_enc.encode(prompt))}...')
            if verbose:
                print('-------- prompt --------')
                print(prompt)
                print('------------------------')
            response = openai.ChatCompletion.create(
                model='gpt-4',
                messages=[{"role": "user", "content": prompt}]
            )
            if verbose:
                print('-------- response --------')
                print(response)
                print('--------------------------')
            yield response
            set_to_cache(prompt, json.dumps(response))
        else:
            print(f'Getting response from cache for prompt of length {len(tiktoken_enc.encode(prompt))}...')
            yield json.loads(data)


def main():
    openai.api_key = os.environ['OPENAI_API_KEY']
    tiktoken_enc = tiktoken.encoding_for_model('gpt-4')
    max_prompt_length = 8192 - 10  # need to reduce by 10 because the real token length appears to be slightly longer
    prompt = None
    while prompt is None:
        try:
            for prompt in prompt_data_aggregator(
                    PROMPT_AGGREGATION_TEXT,
                    (
                        response['choices'][0]['message']['content']
                        for response
                        in iterate_prompt_responses(tiktoken_enc, max_prompt_length)
                    ),
                    tiktoken_enc, max_prompt_length
            ):
                break
        except openai.error.RateLimitError:
            print('Rate limit reached, waiting 10 seconds and retrying (we have cache of previously received responses)...')
            time.sleep(10)
            continue
    print('Done! Processing final prompt')
    # print('-------- prompt --------')
    # print(prompt)
    # print('------------------------')
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{"role": "user", "content": prompt}]
    )
    # print('-------- response --------')
    # print(response)
    # print('--------------------------')
    print(response['choices'][0]['message']['content'])


if __name__ == '__main__':
    main()
