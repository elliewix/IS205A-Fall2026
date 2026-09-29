# write a function that "formats" a name
# func that title cases a name, note that this is very limited
# and return that formatted name
#
# def format_name(name):
#     name = name.title()
#     return name
#
# def greeting(name):
#     my_greeting = "Hello, there, " + name
#     return my_greeting
#
# print(format_name("oliver wickes"))
# print(format_name("OLIVER wickes"))
# print(format_name("OLIVER WICKES"))
# print(greeting(format_name("OLIVER WICKES")))

###
# what if one used the other?

print("calling one func from the other")

def greeting(name):
    my_greeting = "Hello, there, " + format_name(name)
    return my_greeting

def format_name(name):
    name = name.title()
    return name

print(greeting("PHillip"))
print(greeting("oliver wickes"))
print(greeting("OLIVER wickes"))
print(greeting("OLIVER WICKES"))

###
# a moment about booleans
print("True") # this is a string
print(True) # this is a bool

print("cat" in "caterpillar")
def detect_plain(bigstring, term):
    result = term in bigstring
    # return "True" # nope, don't do this
    return result

print(type(detect_plain("cats", "cat"))) # class bool
# if you see class str you need to fix it

print(detect_plain("university catering", "cat"))
