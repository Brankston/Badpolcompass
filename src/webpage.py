from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    text = "Bad Political Compass"
    return 'This is the {text}'

if __name__ == '__main__':
    app.run()
