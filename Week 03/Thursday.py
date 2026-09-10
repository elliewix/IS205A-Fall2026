# set variables

## coordinates

x = 30
y = 20

## other numbers
## like calculating a bill
total_bill = 130 # dollars, setting a var to the total bill
# person 1 pays 30% person 2 pays 15% person 3 pays the rest
# doing calculations with variables

# calculate person 1's share
p1 = total_bill * .3 # 30%
p2 = total_bill * .15 # 15%
p3 = total_bill - (p1 + p2) # the remainder of the bill
p3_percent = total_bill * (1 - (.3 + .15)) # calc the diff

print(p1, p2, p3, p3_percent)

###

# syntax errors, the code just doesn't run
# print("cat" - 1)
# print(100/0)

# semantic errors, did some thing....but not what you wanted
p3_percent = total_bill * (100 - (.3 + .15)) # calc the diff
print(p3_percent, "p3 bill with an error")