import os
from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route("/")
def hello_world():
    return render_template('index.html')
