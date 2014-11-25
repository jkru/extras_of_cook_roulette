import clus
import random
import config_db

class RecipeMachine(object):
    def generate_markov_recipe(self):
        self.markov_chain_dict = config_db.getter()[4]
        self.markov_seed_ingr = random.choice(self.markov_chain_dict.keys())
        self.markov_meal = self.populate_markov_meal()
        self.meal = self.markov_meal
        display_meal = self.nounder()
        return self.meal

    def populate_markov_meal(self):

        ingredient_by_type = config_db.getter()[3]
        
        meal = {"protein":"", "vegetable":"", "starch":""}
        needs_more = True
        my_ingredient = self.markov_seed_ingr
        counter = 0

        while needs_more==True:
            my_list_of_types = ingredient_by_type[my_ingredient]
            my_first_type = my_list_of_types[0]
            meal[my_first_type] = my_ingredient
            my_ingredient = random.choice(self.markov_chain_dict[self.markov_seed_ingr])
            counter +=1
            if counter == 20:
                counter = 1
                my_ingredient = random.choice(self.markov_chain_dict.keys())

            if meal['protein'] != "" and meal['vegetable']!="" and meal['starch']!="":
                needs_more = False
        return meal
        
    def generate_random_recipe(self):
        #congfig_db2 => {protein: chicken, steak}
        self.all_types = config_db.getter()[2]
        while True:
            self.meal = self.make_random_meal()
            complete_meal = self.check_meal()
            display_meal = self.nounder()

            if complete_meal:
                return self.meal
                break

    def make_random_meal(self):
        meal = {}
        for type_, ingredients in self.all_types.iteritems():
            meal[type_] = random.choice(ingredients)
        return meal


    def generate_kmeans_recipe(self):
        while True:
            self.cluster = config_db.getter()[0].keys()
            self.seed_cluster = random.choice(self.cluster)
            self.ingr_sorted_type = self.get_ing_type()
            self.meal = self.make_kmeans_meal()
            complete_meal = self.check_meal()
            display_meal = self.nounder()

            if complete_meal:
                return self.meal
                break

    

    def nounder(self):
        """takes out underscores from names.
        
        Goes through a dictionary and takes out the underscores in all
        of the ingredients (items).

        """
        for type_, item in self.meal.iteritems():
            self.meal[type_] = item.replace("_"," ")
        return self.meal
            
    def get_ing_type(self):
        """returns a dictionary of all of the ingredients in a cluster that
        are sorted based on their type.

        Looks in the dictionary where key=cluste number and value =
        each ingredient. Appends each to the correct type.

        #do something here where it makes the ingredient type based on the
        #global type_dictionary, that has the ingredients categorized by type
        #and then grabs at the ingredients that are in the particular cluster
        #dictionary.
        """

        thisclusterings = config_db.getter()[1][self.seed_cluster]
        alltypes = config_db.getter()[2]
        allingrs = config_db.getter()[3]
        ingr_sorted_type = {}

        this_cluster_types = {}
        
        for ingr in thisclusterings:
            ingr = ingr.replace(" ","_")
            for alltypes in allingrs[ingr]:
                this_cluster_types.setdefault(alltypes,[]).append(ingr)
        return this_cluster_types


    def make_kmeans_meal(self):
        """populates the meal dictionary. 

        goes into the 

        """

        meal = {'vegetable':"",'protein':"",'starch':""}
        for key, value in self.ingr_sorted_type.iteritems():
            if value != "":
                meal[key] = random.choice(self.ingr_sorted_type[key])
        return meal
    
    def check_meal(self):
        """checks to see if there are empty entries in the meal.
        """

        if "" not in self.meal.values():
            return True


#    def get_cluster_data(self):
#        """Finds the associated data rows for the random cluster.
#            
#        """
#
#        cluster_data = []
#        for recipe_id in self.seed_cluster:
#            cluster_data.append(self.data[recipe_id])
#        return cluster_data
#
#
#    def populate_cluster_ingredient_names(self):
#        """Finds human-readable names for all the ingredients of the recipes
#        of the random cluster.
#
#        It takes the dataset of the cluster 
#
#        """
#
#        cluster_ingredients = {}
#        for cluster_recipe in self.cluster_data:
#            for pos, recipe_ingredient in enumerate(cluster_recipe):
#                if recipe_ingredient == 1:
#                    cluster_ingredients[self.all_ingredients[pos]] = cluster_ingredients.get(self.all_ingredients[pos], 0) + 1
#
#        return cluster_ingredients




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




if __name__=="__main__":
    import doctest
    doctest.testmod()
