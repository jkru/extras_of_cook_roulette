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

def check_recipe(ings):
    """check ings.meal attribute to see if there are all types
    """
    #for ingredient_type,random_ingredient in ings.meal.iteritems():
    for ingredient_type in ['vegetable','protein','starch']:
        random_ingredient = ings.ingredient_type
        if random_ingredient != "":
            return ings
        else:
            print "asdfasdf"
            raw_input()
            ings = RecipeMachine()
            return check_recipe(ings)



@app.route("/feedme")
def random_meal():
    ings  = RecipeMachine()
    checked_ings = check_recipe(ings)
    return render_template("random_meal.html",vegetable=checked_ings.vegetable, starch=checked_ings.starch,protein=checked_ings.protein)

if __name__ == "__main__":
#call a function here
#or... look for the flask set up thing

    app.run(debug=True)
