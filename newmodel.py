from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Table
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from passlib.hash import sha256_crypt


engine = create_engine("sqlite:///testcookroulette.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, 
                                      autocommit=False,
                                      autoflush=False))
Base = declarative_base()
Base.query = session.query_property

def connect():
    engine = create_engine("sqlite:///testcookroulette.db", echo=True)
    session = scoped_session(sessionmaker(bind=engine, 
                                      autocommit=False,
                                      autoflush=False))
    return session()

#==================These are 2 tables with backrefs==========/
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    settings = Column(String(64), nullable=True)


def create_user_account(email, password, settings="kmeans"):
    if email =="" or password =="":
        return "Please Fill Out All Fields"
    try:
        #get an "all()" and then see if your list is empty
        existing = session.query(User).filter_by(email=email).first()
        if email == existing.email:
            return "User Already Exists."
    except:
        u = User()
        u.email = email
        u.password = password
        u.settings = settings

        session.add(u)
        session.commit()
        return "Successfully Added!"

def login(email_in, password_in):

    if email_in =="" or password_in =="":
        return "Fill Out All Fields"
    db_return = session.query(User).filter_by(email=email_in).first()
    try:
        db_return.email
        db_pw = db_return.password
        
        if sha256_crypt.verify(password_in,db_pw):
            return "Yay!"
        else:
            return "Incorrect Password"
    except:
        return "Email does not exist"


def change_pw(email_in,newpass):
    u = session.query(User).filter_by(email=email_in).first()
    u.password = newpass
    session.add(u)
    session.commit()
    return "Password Successfully Updated!"
    
class SavedRecipe(Base):

    __tablename__= "savedrecipes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe = Column(String(500), nullable=False)
    rating = Column(String(10))

    user = relationship("User", backref=backref('savedrecipes', order_by=id))

def save_recipe(session_email,saved_meal):
    user_id = session.query(User).filter_by(email=session_email).first().id
    s = SavedRecipe(user_id=user_id, recipe=saved_meal)
    session.add(s)
    session.commit()



def get_list_saved_recipes(session_email):
    user = session.query(User).filter_by(email=session_email).first()
    all_recipes = session.query(SavedRecipe).filter_by(user_id=user.id).all()

    list_of_recipes = []
    for a_recipe in all_recipes:
        list_of_recipes.append(a_recipe)

    return list_of_recipes


#==================These are 3 tables with 2 association tables==========/


recipes_ingredients_association = Table('recipes_ingredients', Base.metadata, Column('recipe_id', Integer, ForeignKey('recipes.id')), Column('ingredient_id', Integer, ForeignKey('ingredients.id')))

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    cluster = Column(Integer, nullable=False)

    ingredients = relationship("Ingredient", secondary=recipes_ingredients_association)

ingredients_types_association = Table('ingredients_types', Base.metadata, Column('ingredient_id', Integer, ForeignKey('ingredients.id')), Column('type_id', Integer, ForeignKey('types_.id')))

class Ingredient(Base):
    __tablename__= "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(40))   # used to be called ingredient


    recipes = relationship("Recipe", secondary=recipes_ingredients_association)
    types_ = relationship("Type_", secondary=ingredients_types_association)

class Type_(Base):
    __tablename__="types_"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    ingredients = relationship("Ingredient", secondary=ingredients_types_association)


def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
