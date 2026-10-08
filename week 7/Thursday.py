infile = open('words.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()

print(lines)

# for l in lines:
#     clean_l = l.strip() # default mode removes spaces
#     print(clean_l, clean_l.strip('?.!")')) # order doesn't matter
#     # all chars treated as sep options
import string
print(string.punctuation)
for l in lines:
    clean_l = l.strip() # default mode removes spaces
    print(clean_l, clean_l.strip(string.punctuation)) # order doesn't matter
    # all chars treated as sep options

### let's talk about outfiles
infile = open('words.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()
# count = 0
# for l in lines:
#     # in HW 3 you'll need to do a few other things
#     clean_l = l.strip() # stripping off newlines
#     clean_text = clean_l.strip(string.punctuation) # remove punc off sides
#     # if filter
#     # print(clean_text.startswith('w')) # see the results
#     # count = count + 1 # nope not here
#     if clean_text.startswith('w') == True:
#         # we only want to see the matches
#         count = count + 1 # count only if positive
#         print(clean_text)
#
# print(count)

# add the outfile pattern

# alone....filename needs to be new and use 'wt'
outfile = open('results.txt', 'wt', encoding='utf-8')
outfile.write("hello here is some text")
outfile.close()

# but we only want the positive matches
outfile = open('the_w_lines.txt', 'wt', encoding='utf-8')

for l in lines:
    clean_l = l.strip() # stripping off newlines
    clean_text = clean_l.strip(string.punctuation) # remove punc off sides
    if clean_text.startswith('w') == True:
        # we only want to see the matches
        outfile.write(clean_text + "\n")

outfile.close()