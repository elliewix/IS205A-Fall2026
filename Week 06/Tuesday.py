import math

def c_to_r_printed(c):
    r = c / (2 * math.pi)
    print(r)

def c_to_r(c):
    r = c / (2 * math.pi)
    return r

# r_in_cm = c_to_r(30) * 2.54
# print(r_in_cm)

c_to_r_printed(30)