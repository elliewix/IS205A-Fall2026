# messing with strings

text = "Get in the robot, Shinji"
# first lowercase, retaining variable name
text = text.lower()
# text.lower() # missing the assignment
print(text)
# next is replace for the comma
text = text.replace(',', "") # "" is empty string
print(text)
# default or "empty" split breaks on
# consecutive/adjacent space characters
print("weird text".split())
print("weird         \t  \n      text".split())

# NOPENOPENOPE
print("weird         \t  \n      text".split(" "))

# be careful, you need to do all your cleaning
# before you split
words = text.split()
# print(words.lower()) # no attribute lower error

sen1 = "I adored the CBTF."
sen2 = "My car is red."
sen3 = "I am taking 17 credits."
sen1 = sen1.lower()
sen2 = sen2.lower()
sen3 = sen3.lower()

# the in keyword with strings
sen1 = "I adored the CBTF."
sen1 = sen1.lower()
print("red" in sen1)
print("cat" in sen1)
print('cbtf' in sen1) # recall we lowered it

# how do we find red but not adored?
# split! changing data types mean new variable name
sen1_words = sen1.split()
sen2_words = sen2.split()
sen3_words = sen3.split()

print('red' in sen1_words) # False
print('red' in sen2_words) # Still false
print('red' in sen3_words) # False
print(sen2_words)
print('red' in "there's red stuff".split()) # True

# solve the punctuation?
# fact 1: we have a string of all the punc
import string
print(string.punctuation)

# fact 2: we loop over strings, we get
# one character at a time, isololating them
for punc in string.punctuation:
    print(punc)

# fact 3: the replace string method takes
# one character at a time
# fact 4: you can use "" to effectively remove something
# erase the punc
sen = "My car is red, Shinji."
for punc in string.punctuation:
    sen = sen.replace(punc, "")
print(sen)
sen = sen.lower()
sen_words = sen.split()
print(sen_words, 'red' in sen_words)


