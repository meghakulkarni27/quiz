from flask import Flask, render_template, request
from questions import quiz_data
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():

    category = request.args.get('category')

    questions = quiz_data[category]

    random.shuffle(questions)

    return render_template(
        'quiz.html',
        questions=questions,
        category=category
    )

@app.route('/result', methods=['POST'])
def result():

    category = request.form['category']

    questions = quiz_data[category]

    score = 0

    for i, q in enumerate(questions):

        user_answer = request.form.get(f'q{i}')

        if user_answer == q['answer']:
            score += 1

    return render_template(
        'result.html',
        score=score,
        total=len(questions)
    )

if __name__ == "__main__":
    app.run(debug=True)