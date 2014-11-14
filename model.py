from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, and_, or_
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.orm import scoped_session
from sqlalchemy import ForeignKey



#'postgresql://julie:ninjabear@localhost:5432/mydatabase'
#thing that makes each session thread-safe
engine = create_engine("sqlite:///cookroulette.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    settings = Column(String(64), nullable=True)

class SavedRecipes(Base):

    __tablename__= "savedrecipes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe = Column(String(500), nullable=False)
    rating = Column(String(10), nullable=True)

    user = relationship("User", backref=backref('savedrecipes', order_by=id))

# Python
# variable_names
# ClassName
# _variable_name
# class_

# JS
# ClassName
# variableName

#index sqla search sort join

###separated tables###

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    cluster = Column(Integer, nullable=False)
#    incl_ingr = Column(String(300))   # FIXME: dont need?
 


class RecipeIngredient(Base):
    __tablename__= "recipes_ingredients"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))   # index
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))   # index

    recipe = relationship("Recipe", backref=backref('recipes_ingredients', order_by=id))
    ingredient = relationship("Ingredient", backref=backref('recipe_ingredients', order_by=id))

class Ingredient(Base):
    __tablename__= "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(40))   # used to be called ingredient

    types_ = relationship("Type", secondary="ingredients_types")


#db.tables syntax
#association_table relationships.html sqla
class IngredientType:
    __tablename__= "ingredients_types"

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingreiends.id', order_by=id))
    type__id = Column(Integer, ForeignKey('types.id', order_by=id))

    ingredient = relationship("Ingredient", backref=backref('ingredients_types', order_by=id))
    type_ = relationship("Type", backref=backref('ingredients_types', order_by=id))

class Type_:
    __tablename__="types"

    id = Column(Integer, primary_key=True)
    type_ = Column(String(16), nullable=False)   # name

    ingredients = relationship("Ingredient", secondary="ingredients_types")

# class IngredientType:
# ingredient_id
# type

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///cookroulette.db", echo=False)
    Session = sessionmaker(bind=ENGINE)
    return Session()


def main():
    pass


if __name__ == "__main__":
    main()
    
