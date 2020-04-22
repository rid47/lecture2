import datetime
from flask import Flask, render_template

app = Flask(__name__)
#print(__name__)


@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    # new_year = True
    # headline = "hello mizan"
    names = ["Alice", "Bob", "Mizan"]
    return render_template("index.html", names=names)


@app.route('/david')
def david():
    return "Hello, David!!"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"


@app.route("/bye")
def bye():
    headline = "Bye"
    return render_template("index.html", headline=headline)


@app.route("/more")
def more():
    return render_template("more.html")


if __name__ == "__main__":
    app.run(debug=True)
