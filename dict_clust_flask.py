import clus
import random

GLOBAL_MEAL = {'vegetable':"",'protein':"",'starch':""}

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
    #print ing_type
    return ing_type


def append_well(food_type_list, amount, ingr):
    for i in range(amount):
        food_type_list.append(ingr)
    return food_type_list

def get_ing_type(cluster_ingredients, ing_type):
    ingr_sorted_type = {'vegetable':"",'protein':"",'starch':""}
    vegetable = []
    protein = []
    starch = []
    for ingr, amount in cluster_ingredients.iteritems():
        if ing_type[ingr][0] == 'vegetable':
            ingr_sorted_type[ing_type[ingr][0]] = append_well(vegetable, amount, ingr)
        elif ing_type[ingr][0] == 'protein':
            ingr_sorted_type[ing_type[ingr][0]] = append_well(protein, amount, ingr)
        elif ing_type[ingr][0] == 'starch':
            ingr_sorted_type[ing_type[ingr][0]] = append_well(starch, amount,ingr)

    #print ingr_sorted_type
    return ingr_sorted_type
#for this cluster, the starches are potatoes, pasta, etc
#for macro in protein, veg, starch:
#go into dictionary and pick a random one from that category


def get_ing_cluster(seed_cluster, data):
    cluster_data = []
    for recipe_id in seed_cluster:
        cluster_data.append(data[recipe_id])
    return cluster_data

def get_ing(cluster_data, ingredients):
    cluster_ingredients = {}
    for cluster_recipe in cluster_data:
        for pos, recipe_ingredient in enumerate(cluster_recipe):
            if recipe_ingredient == 1:
                cluster_ingredients[ingredients[pos]] = cluster_ingredients.get(ingredients[pos], 0) + 1

    return cluster_ingredients

def make_meal(ingr_sorted_type, meal=None):
    if not meal:
        global GLOBAL_MEAL
        meal = GLOBAL_MEAL
    for key, value in ingr_sorted_type.iteritems():
        if value:
            #print key, random.choice(ingr_sorted_type[key])
            meal[key] = random.choice(ingr_sorted_type[key])
        else:
            #print "WARNING"
            GLOBAL_MEAL = meal
            algo_main(meal)

    GLOBAL_MEAL = meal
    return GLOBAL_MEAL

def algo_main(meal=None):
    ###########################################################
    recipe, ingredients, data, kclust = initialize_clusters()
    ing_type = initialize_ingredient_categories()
    ###########################################################
    
    seed_cluster = random.choice(kclust)
    cluster_data = get_ing_cluster(seed_cluster,data)
    cluster_ingredients = get_ing(cluster_data, ingredients)
    ingr_sorted_type = get_ing_type(cluster_ingredients, ing_type)

    if meal:
        meal = make_meal(ingr_sorted_type, meal)
    else:
        meal = make_meal(ingr_sorted_type)
    
    return meal

    ########################################


def main():
    print algo_main()

if __name__=="__main__":
    main()
