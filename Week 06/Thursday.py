# infile pattern

# step 1: tell python about it
infile = open('words.txt', 'rt', encoding = 'utf-8')
# step 2: actually get some content
text = infile.read() # read everything into a string
# step 3: close it
infile.close()
print(text)

# go through things line by line
# step 1 the same
infile = open('words.txt', 'rt', encoding = 'utf-8')
for line in infile:
    print(line)
infile.close()

# range function
# start, stop, step
# start is inclusive
print(list(range(5))) # single value is stop
print(list(range(3, 12))) # start, stop
print(list(range(3, 12, 2)))
print(list(range(11, 3, -1))) # neg step in range

### don't use this on your homework
infile = open('words.txt', 'rt', encoding = 'utf-8')
for _ in range(5):
    print(next(infile))
infile.close()

## diff way of loading
infile = open('words.txt', 'rt', encoding = 'utf-8')
text = infile.read()
infile.close() # totally done with the file, just move on

lines = text.splitlines()
print(lines)

# index on a line, single position
print(lines[6]) # see one index pos? indexing
# indexing on a list gives you that actual object
print(lines[3:7]) # this is slicing, with the :
# you will always get a list back when you slice a list
print(lines[::-1]) # reverse a list
