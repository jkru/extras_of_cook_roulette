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
#remove kclust from class? 
#need to reconstruct data from the input files, but should be easy to do
#all_ingredients not an init thing
#recipe = human readable recipe name
#ingredient_type => chicken is a protein

    def __init__(self):
###################take these things out of the class#########
        self.recipe, self.all_ingredients, self.data, self.kclust, self.ingredient_type = temp_init_function()

#only have protein, veg, etc. in on entry point

    ###################This stuff stays in the class##############

    def generate_kmeans_recipe(self):
        while True:
            self.seed_cluster = random.choice(self.kclust)
            self.cluster_data =  self.get_cluster_data()
            self.cluster_ingredients = self.populate_cluster_ingredient_names()
            self.ingr_sorted_type = self.get_ing_type()
            self.meal = self.make_meal()
            complete_meal = self.check_meal()

            if complete_meal:
                return self.meal
                break

    def get_cluster_data(self):
        """Finds the associated data rows for the random cluster.
            
        """

        cluster_data = []
        for recipe_id in self.seed_cluster:
            cluster_data.append(self.data[recipe_id])
        return cluster_data


    def populate_cluster_ingredient_names(self):
        """Finds human-readable names for all the ingredients of the recipes
        of the random cluster.

        It takes the dataset of the cluster 

        """

        cluster_ingredients = {}
        for cluster_recipe in self.cluster_data:
            for pos, recipe_ingredient in enumerate(cluster_recipe):
                if recipe_ingredient == 1:
                    cluster_ingredients[self.all_ingredients[pos]] = cluster_ingredients.get(self.all_ingredients[pos], 0) + 1

        return cluster_ingredients


    def get_ing_type(self):
        """returns a dictionary of all of the ingredients in a cluster that
        are sorted based on their type.

        looks in the ingredient_type dictionary for each ingredient of the
        cluster_ingredient dictionary and then appends them to the correct
        list.

        """

        ingr_sorted_type = {}

        for ingr, amount in self.cluster_ingredients.iteritems():
            my_ingredient_type = self.ingredient_type[ingr][0]
            ingr_sorted_type.setdefault(my_ingredient_type,[]).extend([ingr]*amount)

        return ingr_sorted_type


    def make_meal(self):
        """populates the meal dictionary.

        goes into the 
        """
        meal = {'vegetable':"",'protein':"",'starch':""}
        for key, value in self.ingr_sorted_type.iteritems():
            if value != "":
                meal[key] = random.choice(self.ingr_sorted_type[key])
        return meal
    
    def check_meal(self):
        if "" not in self.meal.values():
            return True

if __name__=="__main__":
    import doctest
    doctest.testmod()
