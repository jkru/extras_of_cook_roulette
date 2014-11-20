def recipes(ingredientsdict):
    g = open("indexedrecipes.lst","r")
    h = open("recipes_ingredients.txt", "w")
    for i, line in enumerate(g):
        recipeindex = line.split()[0]
        recipe = line.split()[1:]
        for ingredient in recipe:
            ing_index = ingredientsdict[ingredient]
            sql_ing_index = int(ing_index)+1
            h.write(str(sql_ing_index)+" "+str(i)+"\n")
    g.close()
def ingredients():
    f = open("indexedingredients.lst","r")
    ingredients = {}
    for line in f:
        ingredientindex = line.split()[0]
        ingredient = line.split()[1]
        ingredients[ingredient] = ingredientindex

    f.close()    
    return ingredients

def ingredient_types():
    types_ = {'herbspice':1, 'fat':2,'fruit':3, 'liquid':4, 'protein':5, 'starch':6, 'vegetable':7}
    f = open("extracategories.lst", "r")
    h = open("typed.lst","w")
    ingredients = {}
    for line in f:
        ingredientindex = line.split()[0]
        ingredient = line.split()[1]
        ingredient_type = line.split()[2:]
        print ingredient_type
        for it in ingredient_type:
            h.write(ingredientindex+" "+str(types_[it])+"\n")

    f.close()    
    return ingredients


def main():
    #ingredient_dict = ingredients()
    #recipes(ingredient_dict)
    ingredient_types()

if __name__=="__main__":
    main()
