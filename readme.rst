Cook Roulette: A random meal generator
=====================
.. image:: https://raw.githubusercontent.com/jkru/cook_roulette/master/hompage.png

Cook Roulette is a random meal generator that creates combinations of food so you don't have to think about what you should make for dinner.

https://guides.github.com/features/mastering-markdown/


The premise
-----
Cook Roulette randomly generates meals.

The code is run with a shell script::

     ./runscript.scr

This isn't included here, but holds the keys to yummly and twilio.

Web App Features
----------------------- 
1. Log in functionality
2. Save meals
3. Select type of meal generation (k-means, Markov chain, or random)
4. Uses Yummly API to find a recipe that uses those meal ingredients

User Experience
-----------------------
Users can create an account:
.. image:: https://raw.githubusercontent.com/jkru/cook_roulette/master/create_account.png

And then log into the page:
.. image:: https://raw.githubusercontent.com/jkru/cook_roulette/master/login.png

The main part of the page:
.. image:: https://raw.githubusercontent.com/jkru/cook_roulette/master/main_part.png


Extras
-----------------------
1. Text to twilio for a k-means generated meal

2. Outward facing REST-ful API that provides a json object with a generated k-means meal

