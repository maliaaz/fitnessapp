from flask import Flask
from exercise import Exercises
from calories import Calories
import requests
import random

app = Flask(__name__)
@app.route('/')
def intro():
    return "Welcome to Fitness App!"

@app.route('/exerciseplanner')
def exerciseplanner():
    return Exercises()

@app.route('/caloriecounter')
def caloriecounter():
    return Calories()

if __name__ == '__main__':
    app.run(debug=True)