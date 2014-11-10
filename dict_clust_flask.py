import clus
import random

def initialize_clusters():
    recipe, ingredients, data = clus.readfile('testgroup')
    kclust = clus.kcluster(data,k=4)
    return [recipe, ingredients, data, kclust]

def initialize_ingredient_categories():
    ingredient_categories = open('ing_cat.lst','r')

    ing_type = {}
    for ingcat in ingredient_categories:
        ingcat = ingcat.split()
        ing_type[ingcat[0]] = ingcat[1:]
    ingredient_categories.close()
    return ing_type

def get_new_recipe(seed_recipe,seed_cluster):
    new_recipe = random.choice(seed_cluster)
    if new_recipe == seed_recipe:
        return get_new_recipe(seed_recipe,seed_cluster)
    return new_recipe

def get_ingr_list(ingredients, seed_data):
    seed_ingr_list = []
    for j, ind in enumerate(seed_data):
        if ind == 1:
            seed_ingr_list.append(ingredients[j])
    return seed_ingr_list

def get_comp_ing_type(meal, new_ing, seed_ingr,ing_type,ingredients,new_data):
    #gets a new ingredient and checks its type against what's in the meal
    new_ing = random.choice(get_ingr_list(ingredients,new_data))
    print meal, "this is the meal"
    print meal[ing_type[new_ing][0]],"printed mealing"
    if meal[ing_type[new_ing][0]] != "":
        new_ing = random.choice(get_ingr_list(ingredients,new_data))
        return get_comp_ing_type(meal, new_ing,seed_ingr,ing_type,ingredients,new_data)
    return new_ing


#for this cluster, the starches are potatoes, pasta, etc
#for macro in protein, veg, starch:
#go into dictionary and pick a random one from that category

def add_next_ingr(seed_recipe,seed_cluster,ingredients,meal,seed_ingr,ing_type,recipe,data):

    new_recipe = get_new_recipe(seed_recipe,seed_cluster)
    print "new recipe:",new_recipe, recipe[seed_cluster[seed_cluster.index(new_recipe)]]

    new_data = data[seed_cluster[seed_cluster.index(new_recipe)]]
    new_ingr_list = get_ingr_list(ingredients, new_data)
    new_ing = ""
    new_ing = get_comp_ing_type(meal, new_ing, seed_ingr,ing_type,ingredients,new_data)
    meal[ing_type[new_ing][0]]=new_ing
    print meal
#    return meal

def get_ing_cluster(seed_cluster, data):
    cluster_data = []
    for recipe_id in seed_cluster:
        cluster_data.append(data[recipe_id])
    return cluster_data

def get_ing_type(cluster_data, ingredients):
    cluster_ingredients = {}
    for cluster_recipe in cluster_data:
        for pos, recipe_ingredient in enumerate(cluster_recipe):
            if recipe_ingredient == 1:
                cluster_ingredients[ingredients[pos]] = cluster_ingredients.get(ingredients[pos], 0) + 1

    print cluster_ingredients
    raw_input()

def main():
    recipe, ingredients, data, kclust = initialize_clusters()
    ing_type = initialize_ingredient_categories()


    print data        
    print "*****************************************************"
    print "let's try this randomizer business"

    seed_cluster = random.choice(kclust)

    print "seed cluster:",seed_cluster

    cluster_data = get_ing_cluster(seed_cluster,data)
    print cluster_data
    ingredients = get_ing_type(cluster_data, ingredients)

########################################



    meal = {'starch':'','protein':'','vegetable':''}

if __name__=="__main__":
    main()
