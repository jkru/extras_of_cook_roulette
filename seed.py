import model


def load_recipes(session):
    rec_clus = open('short/recipe_cluster.txt')
    all_recipes = []
    for line in rec_clus:
        line = line.strip().split()
        recipe = line[0]
        cluster = line[1]
        aRecipe = model.Recipe()
        aRecipe.id = recipe
        aRecipe.cluster = cluster
        all_recipes.append(aRecipe)
        session.add(all_recipes[i])
    rec_clus.close()

def load_recipeingredients(session):
    pass

def load_ingredients(session):
    ingredient_list = open("categorized.lst", 'r')
    all_ingredients = []
    for i, line in enumerate(ingredient_list):
        line = line.strip().split()
        ingredient = line[0]

        anIngredient = model.Ingredient()
        anIngredient.id = i
        anIngredient.ingredient = ingredient
    ingredient_list.close()

def load_ingredients_types(session):
    pass


def load_types(session):
    all_types = []
    for i, item in enumerate(['herbspice', 'fat','fruit', 'liquid', 'protein', 'starch', 'vegetable']):
        aType = model.Type_()
        aType.id = i
        aType.type_ = item
        all_types.append(aType)
        session.add(all_types[i])



def load_users(session):
    f = open("seed_data/u.user", "r")
    reader = csv.reader(f, delimiter="|")
    all_users = []
    for i, row in enumerate(reader):
        aUser = model.User()
        aUser.id = row[0]
        aUser.age = row[1]
        aUser.gender = row[2]
        aUser.zipcode = row[4]
        all_users.append(aUser)
        session.add(all_users[i])

