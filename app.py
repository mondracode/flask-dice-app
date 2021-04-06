from flask import Flask, render_template
import random
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    current_face = dice()
    image = [i for i in os.listdir(
        'static/images') if i.endswith('.png')][current_face-1]
    print(current_face)
    return render_template('index.html', current_face=current_face)


def dice():
    return random.randint(1, 6)
