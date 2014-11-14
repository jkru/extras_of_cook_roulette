from flask import Flask, request, render_template, make_response
from flask import redirect, url_for
import jinja2
import model
from recipemachine import RecipeMachine



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

    recipe_maker = RecipeMachine()
    ingredients = recipe_maker.generate_recipe()

    return render_template("random_meal.html",vegetable=ingredients['vegetable'], protein=ingredients['protein'],starch=ingredients['starch'])

if __name__ == "__main__":
#call a function here
#or... look for the flask set up thing

    app.run(debug=True)
