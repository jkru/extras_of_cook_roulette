Cook Roulette: A random meal generator
=====================

Cook Roulette is a random meal generator that creates combinations of food so you don't have to think about what you should make for dinner.


The premise
-----
Cook Roulette randomly generates meals.

The code is run with a shell script::

     ./runscript.scr

This isn't included here, but holds the keys to yummly and twilio.

Features
-----------------------
1. Web app
   1. Log in functionality
   2. Save meals
   3. Select type of meal generation (k-means, Markov chain, or random)
   4. Uses Yummly API to find a recipe that uses those meal ingredients

2. Text to twilio for a k-means generated meal

3. Outward facing REST-ful API 
