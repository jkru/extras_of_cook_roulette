from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, and_, or_
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.orm import scoped_session
from sqlalchemy import ForeignKey

#magical shit that makes each session thread-safe
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

class Saved_recipes(Base):

    __tablename__= "saved_recipes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe = Column(String(500), nullable=False)
    rating = Column(String(10), nullable=True)

    user = relationship("User", backref=backref('saved_recipes', order_by=id))


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    cluster = Column(Integer, nullable=False)
    incl_ingr = Column(String(300))

class Recipeingredient(Base):
    __tablename__= "recipeingredients"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))

    recipe = relationship("Recipe", backref=backref('recipes', order_by=id))
    ingredient = relationship("Ingredient", backref=backref('ingredients', order_by=id))

class Ingredient(Base):
    __tablename__= "ingredients"

    id = Column(Integer, primary_key=True)
    ingredient = Column(String(40))
    ingr_type = Column(String(40))
    ingr_type2 = Column(String(40))
    ingr_type3 = Column(String(40))

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
    
