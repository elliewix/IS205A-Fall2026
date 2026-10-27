text = "Hello humans, I am a meat popcicle."

h = 0
e = 0
l = 0
o = 0
for c in text:
    if c == 'h':
        h = h + 1
    elif c == 'e':
        e = e + 1
print(h, e)
# we could do it like this
# but that sucks
# what if we could automate this?

# enter the dict

# empty dict
data = {} # dict()

# add a key
data['1'] = "one"
data['2'] = 'two'
data['3'] = 'tree'
print(data)
# replace a data point
data['3'] = "three"
print(data)

# let's inspect this
print(len(data)) # length is three, three pairs
print(data.keys())
print(data.values())
# don't zip these things back up
# use items instead
# to loop over a dict, use .items()
print(data.items())

# remember multi variable assignment is a thing
x, y = (0, 1)
print(x, y)
first, last = ['Elizabeth', "Wickes"]
print(last, first)

# we can use this to cleanly loop over the dict
for key, value in data.items():
    print('the key is', key, 'and value is', value)

# combining these together.....
# how can we loop over something and populate a dict

text = "Hello humans, I am a meat popcicle."
letters = {}
for c in text:
    letters[c] = 'stuff'
print(letters)
print(letters.keys())
# so we can make keys now.... let's think about counting

# now for some logic
text = "Hello humans, I am a meat popcicle."
letters = {}
for c in text:
    if c in letters: # True, so already in there
        # letters[c] = letters[c] + 1
        letters[c] += 1
    else: # False, not seen yet
        letters[c] = 1 # start at 1 b/c we're looking at one

print(letters)
print(letters['x'])