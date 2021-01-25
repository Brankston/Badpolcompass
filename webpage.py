from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    title_page = "Bad Political Compass"
    return render_template('page.html', title_page=title_page)

if __name__ == '__main__':
    app.run()
