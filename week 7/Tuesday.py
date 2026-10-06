one_word = "book"
print(one_word + "-ish")
sen = "I\n am \tkind of        a book person."
# break this apart
print(sen.split())
for word in sen.split(): # w would also be okay
    print(word + "-ish")

# new pattern time!
# list accumulator pattern
prepped = [] # empty list base, list() or []
for word in sen.split(): # w would also be okay
    prep = word + '-ish'
    # prepped = [] # nope! will erase each time
    prepped.append(prep) # collect the new word
    # print(prepped) # see everything
print(prepped)

# connect back into a sentence
print(" ".join(prepped))


# a new pattern! filtering logic
print("finding small words")
sen = "I\n am \tkind of        a book person."
# want to find "small" words
# use len() to determine length, using length
# 3 and lower are "small words"
for word in sen.split():
    print(word, len(word), len(word) <= 3)