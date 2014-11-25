from flask import Flask, request, render_template, make_response
from flask import redirect, url_for, flash, session
from twilio.rest import TwilioRestClient
import twilio.twiml, os
import jinja2
import newmodel
from recipemachine import RecipeMachine
import json, requests
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.secret_key = 'asdf'

TWILIO_ACCOUNT_SID=os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN=os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER=os.environ.get('TWILIO_NUMBER')

YUMMLY_APP_ID = os.environ.get('YUMMLY_APP_ID')
YUMMLY_APP_KEY = os.environ.get('YUMMLY_APP_KEY')


@app.route("/")
def welcome_page():
    return render_template("index.html")

@app.route("/create")
def display_create_account_page():
    return render_template("create.html")

#request recipe thing

@app.route("/create", methods =['POST'])
def actually_create_account_page():
    email_in = request.form.get("email")
    password_in = request.form.get("password")
    settings_in = request.form.get("settings")    

    password_in_s_h = sha256_crypt.encrypt(password_in)

    adduser = newmodel.create_user_account(email=email_in, password=password_in_s_h, settings=settings_in)
    flash (adduser)
    if adduser == "Successfully Added!":
        return render_template("index.html")
    else:
        return redirect(url_for("display_create_account_page"))

@app.route("/login")
def display_login_page():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def actually_login_page():
    email_in = request.form.get("email")
    password_in = request.form.get("password")

    login = newmodel.login(email_in,password_in)

    flash (login)
    if login != "Yay!":
        print "something isn't right"
        return redirect(url_for("display_login_page"))
    else:
        session['email'] = email_in
        session['logged_in'] = True
        session['default_setting'] = newmodel.session.query(newmodel.User).filter_by(email=email_in).first().settings
        return redirect(url_for("random_meal"))

@app.route("/account")
def show_account_page():
    return render_template("account.html", email=session['email'])

@app.route("/changepw")
def display_change_pw():
    return render_template("changepw.html", email=session['email'])

@app.route("/changepw", methods=['POST'])
def actually_change_pw():
    password_check = request.form.get("oldpassword")
    password_in = request.form.get("newpassword")
    password_in2 = request.form.get("checknewpassword")

    #check old password
    login = newmodel.login(session['email'],password_check)
    if login != "Yay!":
        flash ("Incorrect Password")
        return redirect(url_for("display_change_pw"))

    else:
        if password_in!=password_in2:
            print password_in
            print password_in2
            flash ("New Password Does Not Match")
            return redirect(url_for("display_change_pw"))
        else:
            password_in_s_h = sha256_crypt.encrypt(password_in)
            updatepw = newmodel.change_pw(session['email'],password_in_s_h)
            flash (updatepw)
            return redirect(url_for("show_account_page"))

@app.route("/displaysaved")
def display_saved_recipes():
    user = newmodel.session.query(newmodel.User).filter_by(email=session['email']).first()
    all_recipes = newmodel.session.query(newmodel.SavedRecipe).filter_by(user_id=user.id).all()

    list_of_recipes = []
    for a_recipe in all_recipes:
        list_of_recipes.append(a_recipe)
    
    return render_template("saved_recipes.html", recipes=list_of_recipes)


@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")


@app.route("/feedme")
def random_meal():
    recipe_maker = RecipeMachine()

    
    recipe_method = request.args.get("settings")
    if recipe_method == "kmeans":
        ingredients = recipe_maker.generate_kmeans_recipe()
    elif recipe_method == "markov":
        ingredients = recipe_maker.generate_markov_recipe()
    elif recipe_method=="random":
        ingredients = recipe_maker.generate_random_recipe()
    else:
        recipe_method = session['default_setting']
        if recipe_method == "kmeans":
            ingredients = recipe_maker.generate_kmeans_recipe()
        elif recipe_method == "markov":
            ingredients = recipe_maker.generate_markov_recipe()
        else:
            ingredients = recipe_maker.generate_random_recipe()            
    
    #except:
    #    recipe_method = session['default_setting']

    print "in the first try"

    session['meal'] = ingredients

    if request.args.get("yummlycheck") == "yes":
        yummly_api_request = requests.get('http://api.yummly.com/v1/api/recipes?_app_id='+YUMMLY_APP_ID+'&_app_key='+YUMMLY_APP_KEY+'&q='+str(ingredients['vegetable'])+'%2C+'+str(ingredients['protein'])+'%2C+'+str(ingredients['starch'])+'&requirePictures=true')
        json_text = yummly_api_request.text
        json_object = json.loads(json_text)

        try:

            end_of_url = json_object['matches'][0][u'id']
            large_image =  json_object['matches'][0][u'imageUrlsBySize'][u'90'].replace('=s90-c','=s730-e365')
            yummly_rec_name = json_object['matches'][0][u'recipeName']
        except:
            end_of_url = ""
            large_image = "http://upload.wikimedia.org/wikipedia/commons/1/18/Yummly_logo.png"
            yummly_rec_name = "Why don't you try"

        return render_template("random_meal.html",vegetable=ingredients['vegetable'], protein=ingredients['protein'],starch=ingredients['starch'],yummly_image_url=large_image,end_of_url=end_of_url,recipe_name=yummly_rec_name,recipe_method=recipe_method)
    else:              
        return render_template("random_meal.html",vegetable=ingredients['vegetable'], protein=ingredients['protein'],starch=ingredients['starch'],yummly_image_url="",end_of_url="",recipe_method=recipe_method)



@app.route('/saveme')
def save_recipe():
    saved_meal =  json.dumps(session['meal'])
    print saved_meal
    user_id = newmodel.session.query(newmodel.User).filter_by(email=session['email']).first().id
    s = newmodel.SavedRecipe(user_id=user_id, recipe=saved_meal)
    newmodel.session.add(s)
    newmodel.session.commit()

    return redirect(url_for("random_meal"))

@app.route('/twilio', methods=['GET','POST'])
def hello_custom():
    recipe_maker = RecipeMachine()
    ingredients = recipe_maker.generate_kmeans_recipe()
    mess1 = str(ingredients['vegetable'])
    mess2 = str(ingredients['protein'])
    mess3 = str(ingredients['starch'])
    message = mess1+" "+mess2+" "+mess3
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)


@app.route('/api')
def random_api():
    recipe_maker = RecipeMachine()
    ingredients = recipe_maker.generate_kmeans_recipe()
    meal_list = [ingredients['vegetable'], ingredients['protein'],ingredients['starch']]
    #meal_json = json.dump(meal_list)
    mess1 = str(ingredients['vegetable'])
    mess2 = str(ingredients['protein'])
    mess3 = str(ingredients['starch'])
    stupid = '{"meal":{"protein":"'+mess2+'","vegetable":"'+mess1+'","starch":"'+mess3+'"}}'

    return render_template("api.html", meal_json=stupid)

if __name__ == "__main__":
    

    print "INIT"
    app.run(debug=True)



