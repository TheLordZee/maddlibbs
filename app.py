from stories import Story, story
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def story_form():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def display_story():
    answers = {}
    for key in request.args:
        answers[key] = request.args[key]
    new_story = story.generate(answers)
    return render_template('story.html', story=new_story)