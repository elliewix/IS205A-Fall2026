# basic outfile pattern

outfile = open('thursdayresults.gremlinmode.cats', 'wt', encoding='utf-8')
outfile.write("wickes what's wrong with you")
outfile.close()

# people will shortcut things sometimes to
# text = open('horse.txt').read()
# but don't for us

### let's see this in a loop

text = "hello I am a human and not a horse"
# for c in text:
#     print(c, chr(ord(c) + 5))

outfile = open('secret.txt', 'wt', encoding='utf-8')
for c in text:
    # print(c, chr(ord(c) + 5))
    outfile.write(chr(ord(c) + 5))
outfile.close()

secrets = ["some secret", "horses exist", "more coffee"]
# I can make one file with this
outfile = open('secrets.txt','wt', encoding='utf-8')
for s in secrets:
    for c in s:
        offset = chr(ord(c) + 6)
        outfile.write(offset)
    outfile.write('\n')
outfile.close()

# but what about diff files for each?
# one file per cipher?

for num in [4, 5, 6]:
    print(num)
    outfile = open(str(num) + ".txt", 'wt', encoding='utf-8')
    for s in secrets:
        for c in s:
            offset = ord(c) + num
            outfile.write(chr(offset))
        outfile.write('\n')
    outfile.close()