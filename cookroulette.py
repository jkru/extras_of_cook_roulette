from flask import Flask, request, render_template, make_response
from flask import redirect, url_for
import jinja2
from dict_clust_flask import algo_main

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
    ings  = algo_main()
    print ings
    return render_template("random_meal.html",vegetable=ings['vegetable'], starch=ings['starch'],protein=ings['protein'])

if __name__ == "__main__":
    app.run(debug=True)
