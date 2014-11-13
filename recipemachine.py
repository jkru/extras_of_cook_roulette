import clus
import random

def initialize_clusters():
    """Initialize the kmeans clusters and read in data. 
    This is going to get taken out soon.

    This uses a kmeans clustering algorithm to classify recipes into
    different clusters based on their ingredients. 

    returns: a list of the recipes, ingredients, association of
    ingredient inclusion to recipe, and cluster membership

    """
    recipe, all_ingredients, data = clus.readfile('testgroup')
    kclust = clus.kcluster(data,k=4)
    return [recipe, all_ingredients, data, kclust]

def initialize_ingredient_categories():
    """Initializes the individual ingredients by type. This will need to
    be modified, but will likely make use of the dictionaries and not the
    databases.

    """


    ingredient_categories = open('ing_cat.lst','r')

    ingredient_type = {}
    for ingcat in ingredient_categories:
        ingcat = ingcat.split()
        ingredient_type[ingcat[0]] = ingcat[1:]
    ingredient_categories.close()
    return ingredient_type

def temp_init_function():
    """temporary initialization code"""
    recipe, all_ingredients, data, kclust = initialize_clusters()
    ingredient_type = initialize_ingredient_categories()

    return [recipe,all_ingredients,data,kclust,ingredient_type]


class RecipeMachine(object):
    def __init__(self):
        self.recipe, self.all_ingredients, self.data, self.kclust, self.ingredient_type = temp_init_function()
        self.seed_cluster = random.choice(self.kclust)
        self.cluster_data =  get_cluster_data(self.seed_cluster,self.data)
        self.cluster_ingredients = populate_cluster_ingredient_names(self.cluster_data, self.all_ingredients)
        self.ingr_sorted_type = get_ing_type(self.cluster_ingredients, self.ingredient_type)
        self.meal = self.make_meal()
        self.vegetable = self.meal['vegetable']
        self.protein = self.meal['protein']
        self.starch = self.meal['starch']

    def make_meal(self):
        """populates the meal dictionary            
        """
        meal = {'vegetable':"",'protein':"",'starch':""}
        for key, value in self.ingr_sorted_type.iteritems():
            if value != "":
                meal[key] = random.choice(self.ingr_sorted_type[key])
            if value == "":
                print "DOING AN INIT"
#            else:
                self.__init__()
        return meal



def initialize_clusters():
    """Initialize the kmeans clusters and read in data. 
    This is going to get taken out soon.

    This uses a kmeans clustering algorithm to classify recipes into
    different clusters based on their ingredients. 

    returns: a list of the recipes, ingredients, association of
    ingredient inclusion to recipe, and cluster membership

    """
    recipe, all_ingredients, data = clus.readfile('testgroup')
    kclust = clus.kcluster(data,k=4)
    return [recipe, all_ingredients, data, kclust]

def initialize_ingredient_categories():
    """Initializes the individual ingredients by type. This will need to
    be modified, but will likely make use of the dictionaries and not the
    databases.

    """


    ingredient_categories = open('ing_cat.lst','r')

    ingredient_type = {}
    for ingcat in ingredient_categories:
        ingcat = ingcat.split()
        ingredient_type[ingcat[0]] = ingcat[1:]
    ingredient_categories.close()
    return ingredient_type


def append_well(food_type_list, amount, ingr):
    """

    This is basically an extend. It takes the food_type_list and adds
    all the ingredients that fall within the food type.

    """
    for i in range(amount):
        food_type_list.append(ingr)
    return food_type_list

def get_ing_type(cluster_ingredients, ingredient_type):
    """returns a dictionary of all of the ingredients in a cluster that
    are sorted based on their type.

    looks in the ingredient_type dictionary for each ingredient of the
    cluster_ingredient dictionary and then appends them to the correct
    list.

    """

    ingr_sorted_type = {'vegetable':"",'protein':"",'starch':""}
    vegetable = []
    protein = []
    starch = [] 
    for ingr, amount in cluster_ingredients.iteritems():
        my_ingredient_type = ingredient_type[ingr][0]
        if my_ingredient_type == 'vegetable':
            ingr_sorted_type[my_ingredient_type] = append_well(vegetable, amount, ingr)
        elif my_ingredient_type == 'protein':
            ingr_sorted_type[my_ingredient_type] = append_well(protein, amount, ingr)
        elif my_ingredient_type == 'starch':
            ingr_sorted_type[my_ingredient_type] = append_well(starch, amount,ingr)

    return ingr_sorted_type


def get_cluster_data(seed_cluster, data):
    """Finds the associated data rows for the random cluster.

    """

    cluster_data = []
    for recipe_id in seed_cluster:
        cluster_data.append(data[recipe_id])
    return cluster_data

def populate_cluster_ingredient_names(cluster_data, all_ingredients):
    """Finds human-readable names for all the ingredients of the recipes
    of the random cluster.

    It takes the dataset of the cluster 

    """

    cluster_ingredients = {}
    for cluster_recipe in cluster_data:
        for pos, recipe_ingredient in enumerate(cluster_recipe):
            if recipe_ingredient == 1:
                cluster_ingredients[all_ingredients[pos]] = cluster_ingredients.get(all_ingredients[pos], 0) + 1

    return cluster_ingredients



def algo_main(meal=None):
    """main part of the algorithm. this is going to be replaced by a
    class.
    """
    ###########################################################
    ###########################################################
    
    seed_cluster = random.choice(kclust)
    cluster_data = get_cluster_data(seed_cluster,data)
    cluster_ingredients = populate_cluster_ingredient_names(cluster_data, all_ingredients)
    ingr_sorted_type = get_ing_type(cluster_ingredients, ingredient_type)

    if meal:
        meal = make_meal(ingr_sorted_type, meal)
    else:
        meal = make_meal(ingr_sorted_type)
    
    return meal

    ########################################


if __name__=="__main__":
    import doctest
    doctest.testmod()
