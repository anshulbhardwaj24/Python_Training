# Opening the file with absolute path
f = open("Document.txt", 'r')
# read file
print(f.read())

# reading a part of file
print(f.read(5))
# move to 11 character
f.seek(11)

# get current position of file handle
print(f.tell()) # 11

# read from 11th character
print(f.read())

# move to the front again
f.seek(0)
# read a single line
print(f.readline())

# Read file into a list
print(f.readlines())	

# Closing the file after reading
f.close()

f = open("demofile2.txt", "a")
# to reduce the size of character in file.
f.truncate(20)
f.close()

# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)

#open and read the file after the truncate:
f = open("demofile2.txt", "r")
print(f.read())

with open('Document.txt','r') as f:
    print(f.read())