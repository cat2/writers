from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']

    # Use GPT-3.5-turbo engine
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    generated_text = chat_completion["choices"][0]["message"]["content"]
    return render_template('index.html', user_input=user_input, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
