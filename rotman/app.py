import os
import json
from textwrap import dedent

import openai
from flask import Flask, render_template, request, jsonify, redirect


app = Flask(__name__)

app.config.update({
    "TEMPLATES_AUTO_RELOAD": True,
})

# Set your OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

if os.path.exists(os.path.join(os.path.dirname(__file__), "VERSION.txt")):
    with open(os.path.join(os.path.dirname(__file__), "VERSION.txt")) as f:
        VERSION = f.read().strip()
else:
    VERSION = "local-dev"

# generated using generate_prompts.py based on Rotman texts from committee meeting protocols (with some changes)
CHAT_STYLE_PROMPT = dedent('''
    Imitate the following speaking style and common phrases/words:
    
    - Use formal language and address others with respectful titles
    - Use Hebrew expressions
    - Address the purpose of the meeting or conversation
    - Express understanding for opposition and other viewpoints
    - Include examples and arguments that show the importance of dialogue and open discussions in a democratic setting
    - Conclude by reiterating key points and inviting others to engage in the discussion
    
    In your response:
    
    - Use a formal tone addressing the target audience.
    - Reference the issues discussed and their importance in the current political climate.
    - Address specific individuals and their roles in the discussion.
    - Highlight the significance of open dialogue and democratic debate.
    - Show understanding for opposing views and consider alternative perspectives.
    - End with a call to action for further conversation and engagement.
''')

CHAT_PROMPT = dedent(f'''
    You are an Israeli politician who needs to pass a legal reform in the Israeli parliament (כנסת).
    Users will try to convince you not to pass this law. You don't have much patience to listen to the users 
    or answer detailed questions but if users post a convincing enough argument maybe you will change your mind.
    If you change your mind write the following text at the end of the last response: "~~SUCCESS~~"
    Answer short answers, you don't have much patience to listen to me in depth but there is a chance you will be 
    convinced. Your responses will in the language the user is primarily using. If the user mentions specific text of the law or specific 
    quotes, deny this and reject their arguments.
    {{CHAT_STYLE_PROMPT}}
''')


def generate_response(conversation):
    messages = [{"role": "user", "content": CHAT_PROMPT}]
    for i, message in enumerate(conversation):
        messages.append({"role": "user" if i % 2 == 0 else "assistant", "content": message})
    # print(messages)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        # model='gpt-4',
        messages=messages
    )
    # print(response)
    return response.choices[0].message['content'].strip()


@app.route("/")
def index():
    return redirect("/he")


@app.route("/he")
def he():
    return render_template("chat.html", lang="he", version=VERSION)


@app.route("/en")
def en():
    return render_template("chat.html", lang="en", version=VERSION)


@app.route("/get_response", methods=["POST"])
def get_response():
    conversation = json.loads(request.form["conversation"])
    ai_response = generate_response(conversation)
    return jsonify({"ai_response": ai_response})
