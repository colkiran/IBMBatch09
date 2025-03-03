
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<usrname>")
def user(usrname):
    return f" <h3> Greetings Mr.{usrname}, Welcome to Flask Programming... </h3> "

if __name__ == '__main__':
    app.run(debug=True)
