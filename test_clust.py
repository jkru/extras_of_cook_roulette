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

def main():
    recipe, ingredients, data, kclust = initialize_clusters()
    ing_type = initialize_ingredient_categories()

    cluster_recipes = []
    for i in range(len(kclust)):
        cluster_recipes_temp = []
        cluster_recipes_temp.append(str(i)+str(" "))
        for r in kclust[i]:
            cluster_recipes_temp.append(recipe[r])
        cluster_recipes.append(cluster_recipes_temp)
    print data        
    print ingredients
    print kclust
    print "these are the clusters"
    print cluster_recipes


    print "let's see what's in the first cluster"
    print "kclust[0] is a list of the items in the first cluster"

    for i in range(len(kclust[0])):
        print "recipe id: ",kclust[0][i]
        #print "recipe: ",recipe[kclust[0][i]]
        print "ingredients in",recipe[kclust[0][i]],"recipe"
        for j, ind in enumerate(data[kclust[0][i]]):
            if ind == 1:
                print ingredients[j]
########################################
    print "*****************************************************"
    print "let's try this randomizer business"

    #print ing_type

    seed_cluster = random.choice(kclust)

    print "seed cluster:",seed_cluster
    seed_recipe = random.choice(seed_cluster)
    seed_recipe_name = recipe[seed_cluster[seed_cluster.index(seed_recipe)]]
    seed_data = data[seed_cluster[seed_cluster.index(seed_recipe)]]
    print "seed recipe",seed_recipe, seed_recipe_name
    print "seed data",seed_data

########################################

    seed_ingr_list = get_ingr_list(ingredients, seed_data)

    print "ingredients in seed recipe:",seed_ingr_list

    seed_ingr = random.choice(seed_ingr_list)


    print "random ingredient and type:",seed_ingr, ing_type[seed_ingr]

    meal = {'starch':'','protein':'','vegetable':''}

    meal[ing_type[seed_ingr][0]] = seed_ingr

    print "meal contents:",meal
    for i in range(len(meal)-1):
        add_next_ingr(seed_recipe,seed_cluster,ingredients,meal,seed_ingr,ing_type,recipe,data)

#    new_recipe = get_new_recipe(seed_recipe,seed_cluster)
#    print "new recipe:",new_recipe, recipe[seed_cluster[seed_cluster.index(new_recipe)]]
#
#    new_data = data[seed_cluster[seed_cluster.index(new_recipe)]]
#    new_ingr_list = get_ingr_list(ingredients, new_data)
#    new_ing = ""
#    new_ing = get_comp_ing_type(meal, new_ing, seed_ingr,ing_type,ingredients,new_data)
#    meal[ing_type[new_ing][0]]=new_ing
#    print meal


###I don't know what the thing is called
#    for type_of_ingr, ingr in meal.iteritems():
#        if ingr == '':
#            print "ing type to fill in meal:",type_of_ingr 



    #print new_ing

if __name__=="__main__":
    main()
