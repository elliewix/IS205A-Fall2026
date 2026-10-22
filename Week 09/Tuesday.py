words = ['lion', 'platapus', 'elephant', 'wombat']
numbers = ['45', '99', '34']

# look at a super small nested loop
for w in words: # outer loop
    print(w, "outline loop print")
    for n in numbers: # inner loop
        print(w, n)

print("Let's invert that")

for n in numbers:
    print(n)
    for w in words:
        # print(w, n)
        print(n, w)

    """
    select *, count(____) from table 
    group by ____
    """
    """
    df.groupby(___)['____'].math()"""

# say we want to make text files for each word
# and then put some data about them in each

# what should be outer loop be?
# likely most of the time, the thing with the labels
# should be your outer one
for w in words:
    print(w + '.txt') # print the proposed file name
    # let's add an outfile pattern within this loop

# create outfile, remember close at the same indent level
#
# for w in words:
#     filename = w + '.txt'
#     outfile = open(filename, 'wt', encoding='utf-8')
#     outfile.write("hello there " + w)
#     outfile.close()

# we can now make 4 files
words = ['lion', 'platapus', 'elephant', 'wombat', 'snake', 'horse']
# we can add terms and the files auto made
# now let's add a for loop inside to generate content
for w in words:
    filename = w + '.txt'
    outfile = open(filename, 'wt', encoding='utf-8')
    print(w)
    for n in numbers:
        text = "there are " + n + " " + w + "s\n"
        outfile.write(text)
    outfile.close()

