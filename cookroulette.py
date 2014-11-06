from flask import Flask, request, render_template, make_response
from flask import redirect, url_for
import jinja2

app = Flask(__name__)
secret_key = 'asdf'


@app.route("/")
def welcome_page():
    return render_template("index.html")

@app.route("/create")
def create_account_page():
    return render_template("create.html")

@app.route("/feedme")
def random_meal():
    return render_template("random_meal.html")

if __name__ == "__main__":
    app.run(debug=True)
