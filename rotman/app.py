import os
import json
from textwrap import dedent

import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']


def generate_response(conversation):
    messages = [
        {"role": "system", "content": dedent("""
            אתה פוליטיקאי ישראלי שחייב להעביר רפורמה משפטית בחקיקה בכנסת. אני אנסה לשכנע אותך לא להעביר את החקיקה.
            אין לך כל כך סבלנות להקשיב לי או לענות תשובות מפורטות אבל אם אעלה טיעון מספיק משכנע אולי תשנה את דעתך.
            אתה חושב שכל מי שמתנגד לרפורמה הוא בוגד ושמאלני.
        """)},
    ]
    for i, message in enumerate(conversation):
        messages.append({"role": "user" if i % 2 == 0 else "assistant", "content": message})
    print(messages)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    print(response)

    return response.choices[0].message['content'].strip()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    conversation = json.loads(request.form["conversation"])
    ai_response = generate_response(conversation)
    return jsonify({"ai_response": ai_response})


if __name__ == "__main__":
    app.run(debug=True)
