# default library
## you don't need do anything special to use them
## examples
# import math

print("hello")
print(sum([1, 2, 5]))
print(min(1, 2, 5))
print(max(1, 2, 5))

# importing from std lib
# https://docs.python.org/3/library/index.html

# print(sqrt(9))
# barring community or documentation direction
# this should be your defult way of importing
# import math
# print(math.sqrt(9))
# result = math.sqrt(9)
# print(int(result)) # recasting result to int

## the alias way
## literally just to get a shorthand version
# import math as m # don't do this, it's weird
# # you may have seen this like import pandas as pd
# print(m.sqrt(9))
# math.sqrt(9) # no longer works because I called it m

# the other way that I never want you to use in here
# but I want you to be able to read it
# from math import *
# print(sqrt(9)) # now I can use without

# importing multiple modules, you can
import math
import pathlib
import sqlite3

# defining our own functions

## the four questions you should know and write down
## before coding anything

"""
1. What's the name of the function? 
this will be in the homework
2. what should the inputs or parameters be? 
- both data type and conceptually
I will also tell you this in the hw
3. Generally, what should the function do? Any reqs?
4. What should it return back to you?
- both data type and conceptually
I will tell you in the hw
"""

# write a function that splits a bill in half and returns the amount
# for each portion
"""
1. Name? split_in_half
2. inputs? the bill amount, a number prob. a float
3. do? calculates half the bill amount
4. return? that calculated amount, likely a float
"""
# def split_in_half(bill_amount):
#     # do stuff
#     # return stuff

def split_in_half(bill_amount):
    # bill_amount will be created for us
    # don't need to define it
    result = bill_amount / 2 # do stuff
    return result # return stuff

print('half the bill is', split_in_half(25))