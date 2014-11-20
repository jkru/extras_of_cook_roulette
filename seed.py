import newmodel

def load_recipes(session):
    rec_clus = open('short/recipe_cluster.lst')
    all_recipes = []
    for line in rec_clus:
        line = line.strip().split()
        recipe = line[0]
        cluster = line[1]
        aRecipe = newmodel.Recipe(id=recipe, cluster=cluster)
        newmodel.session.add(aRecipe)
        newmodel.session.commit()
    rec_clus.close()


def load_ingredients(session):
    ingredient_list = open("categorized.lst", 'r')
    all_ingredients = []
    for i, line in enumerate(ingredient_list):
        line = line.strip().split()
        ingredient = line[0]
        anIngredient =  newmodel.Ingredient(name=ingredient)
        newmodel.session.add(anIngredient)
        newmodel.session.commit()
    ingredient_list.close()


def load_types(session):
    all_types = []
    for item in ['herbspice', 'fat','fruit', 'liquid', 'protein', 'starch', 'vegetable']:
        aType = newmodel.Type_(name=item)
        newmodel.session.add(aType)
        newmodel.session.commit()

def main(session):
#    load_types(session)
#    load_ingredients(session)
    load_recipes(session)

if __name__ == "__main__":
    s = newmodel.connect()
    main(s)
