from random import *

print(choice(['dog', 'cat', 'snake']))

# choice = "bunny"

print(choice)
print(choice(['dog', 'cat']))

from secretstuff import *

print(password)
print(username)
print(stuff())

##

# def demo(name, repeat):
#     text = name * repeat# do stuff
#     print(text)
#     # return
#
# demo("Elizabeth", 3)

def addthese(num1, num2):
    total = num1 + num2
    print(total)
    return total
    print(total)

number_total = 0
for num in [1,2,3,4]:
    number_total = number_total + addthese(10, num)
print(number_total)