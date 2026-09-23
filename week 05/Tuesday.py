stationery = ['black de', 'chalk', 'red de',
              'chalk', 'blue h', 'yellow h']
print(len(stationery))
# now we have something to work with
for pen in stationery:
    # first thing is to print iterable
    print(pen)

# calculate the average length of each string
# pen_count = 0 # base, step 1, before and outside of for loop
# length_sum = 0 # this is an accumulator
# for pen in stationery:
#     # length_sum = len(pen) # not like this
#     length_sum = length_sum + len(pen)
#     print(pen, len(pen), length_sum)
# print(length_sum, "is the total length")
stationery = ['black de', 'chalk', 'red de',
              'chalk', 'blue h', 'yellow h', 'blue pen']
pen_count = 0 # base, step 1, before and outside of for loop
length_sum = 0 # this is an accumulator
for pen in stationery:
    length_sum = length_sum + len(pen)
    pen_count = pen_count + 1
    print(pen, len(pen), length_sum)
print(length_sum, "is the total length")
print(pen_count, "is the total number of pens")

print("the avg length is", length_sum / pen_count)

print(len("snakes"))