"""
modules are an extremely useful tool for organizing and reusing code.
simply put, a module is a python file that contains code, variables, functions, classes 
that you can inclute in another program
just like functions modules help make your code: 
-reusable
-organized
-easier to maintain

DRY principle - "dont repeat yourself"

examples of built in modules:
time, random, os, math.......

eg.
inport math #include module
print(math.pi) #using code from imported module
"""
#import math
#lets see the built in modules:
#help("modules")
#help(math)

#import just one function from a module
from random import randint
#import a module with an alias
import math as m
print(m.pi)

#we could also import just specific functions from a module

print(randint(5,10))