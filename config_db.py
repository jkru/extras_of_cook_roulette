import newmodel

global CLUSTERS 
CLUSTERS = None
global CLUSTER_INGREDIENTS
CLUSTER_INGREDIENTS = None
global TYPE_DICTIONARY
TYPE_DICTIONARY = None
global INGR_TYPE
INGR_TYPE = None

def get_recipes_in_clusters():
    """makes a dictionary of clusters

    Queries the recipe table and creates a dictionary with 
    key = cluster, value = recipes in the cluster.

    """
    allrecipes = newmodel.session.query(newmodel.Recipe).all()
    clusters = {}
    for recipe in allrecipes:
        if clusters.get(recipe.cluster,0) != 0:
            clusters[recipe.cluster] == clusters[recipe.cluster].append(recipe.id)
        else:
            recipelist = []
            recipelist.append(recipe.id)
            clusters[recipe.cluster] = recipelist
    return clusters
        
def get_ingredients_in_clusters(clusters):
    cluster_ingredients = {}
    for cluster, recipes in clusters.iteritems():
        cluster_recipes_ingredients = []
        for recipe in recipes:
            a_recipe =  newmodel.session.query(newmodel.Recipe).filter_by(id=recipe).all()
            the_ingredients = a_recipe[0].ingredients
            ingredients_list = []
            for an_ingredient in the_ingredients:
                no_under_ingred= an_ingredient.name.replace("_"," ")
                ingredients_list.append(no_under_ingred)
            cluster_recipes_ingredients.extend(ingredients_list)
        cluster_ingredients[cluster] = cluster_recipes_ingredients
    return cluster_ingredients
        

def cluster_ingredients():
    clusters = get_recipes_in_clusters()
    cluster_ingredients = get_ingredients_in_clusters(clusters)
    return cluster_ingredients

def ingredient_types():
    all_types = newmodel.session.query(newmodel.Type_).all()    

    type_dictionary = {}

    for a_type in all_types:
        types_list = []
        typed_ingredients = a_type.ingredients
        for my_ingredient in typed_ingredients:
            types_list.append(my_ingredient.name)
        type_dictionary[a_type.name] = types_list
    return type_dictionary


def types_ingredients():
    all_ingrs = newmodel.session.query(newmodel.Ingredient).all()    

    ingr_dictionary = {}

    for an_ingr in all_ingrs:
        ingr_list = []
        associated_types = an_ingr.types_
        for my_type in associated_types:
            ingr_list.append(my_type.name)
        ingr_dictionary[an_ingr.name] = ingr_list
    return ingr_dictionary



def getter():
    """Getter function for the dictionaries that contain the meal generation dictionaries.
    
    looks for the global variables. 
"""

    global CLUSTERS
    global CLUSTER_INGREDIENTS
    global TYPE_DICTIONARY
    global INGR_TYPE
    if CLUSTERS is None:
        CLUSTERS = get_recipes_in_clusters()
        CLUSTER_INGREDIENTS = get_ingredients_in_clusters(CLUSTERS)
        TYPE_DICTIONARY = ingredient_types()
        INGR_TYPE = types_ingredients()
    return [CLUSTERS, CLUSTER_INGREDIENTS, TYPE_DICTIONARY, INGR_TYPE]


#set globals = None
#if globals = None
#do the fucntions to get the dictionaries
#else return globals

#instead of returns, global blah blah = dictionary

#getters to return variables

if __name__=="__main__":
    main()
    