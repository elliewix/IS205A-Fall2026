text = "Hello humans, I am a meat popcicle."

# the actual prepopulation
characters = {}
for c in text:
    characters[c] = 0
print(characters)
# note that I'm not recreating characters = {}
# now I can loop again and count
for c in text:
    characters[c] += 1
print(characters)

# there is sort of a shortcut....
# this is not the prepopulation pattern so don't
# use it in the homework
data = {}
for c in text:
    data.setdefault(c, 0)
    data[c] += 1
print(data)

# so in hw4 you'll have terms and lines
words = text.split()
letters = ['a', 'e', 'i', 'o', 'u'] # and vowels
print(words)
# an alternative prepop is to populate with the universe
# rather than just what we have measured or seen
# vowels = {}
# for l in letters:
#     vowels[l] = 0
# print(vowels)
# for l in letters:
#     for w in words:
#         w = w.lower()
#         if w.startswith(l):
#             vowels[l] += 1
# print(vowels)

letters = ['a', 'e', 'i', 'o', 'u', 'p'] # and vowels
vowels = {}
for l in letters:
    vowels[l] = 0
print(vowels)
text = "I am an extra meat popsicle and I'm here to party."
words = text.split()
for l in letters: # letters to become the files
    filename = l + '.txt'
    print(filename) # make it here, don't explode your computer
    outfile = open(filename, 'wt', encoding='utf-8')
    for w in words:
        # print(filename) # don't make outfile here
        w = w.lower()
        # do I write here? no, this would be every word
        if w.startswith(l):
            vowels[l] += 1
            # do I write here? yes! this is my filter for pos matches
            outfile.write(w + "\n")
        # do I write here? still no
    outfile.close()
print(vowels)