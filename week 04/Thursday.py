"""
1. Name? split_prop
2. inputs? total_bill, num_people
3. do? split a total bill by the number of people
4. Return? a single portion, result of the calc
"""

water = 70

def split_prop(total_bill, num_people):
    result = total_bill / num_people # do stuff
    return result # and return

ameren = 150
people = 3
bill_result = split_prop(ameren, people)
print(bill_result)
print(split_prop(water, 3))
print(split_prop(80, 3))

# printing from a function

def say_hello(name):
    print("hello", name)
    return 3.14159

say_hello("Elizabeth")
print(say_hello("Dave"))
pi = say_hello("Hunter")
print(pi ** 2)

