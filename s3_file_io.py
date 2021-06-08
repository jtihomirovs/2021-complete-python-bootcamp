# First we open this file
myfile = open('myfile.txt')
res = myfile.read()
print(res)

# Go back to the beginning of the file
res = myfile.seek(0)

# Read - to read as a string
# ReadLines - to reads as a list
res = myfile.readlines()
print(res)

# In the end we close this file
myfile.close()

# Second way how to work with files

# mode r - just read
with open('myfile.txt', mode='r') as f:
    print(f.read())

# mode a - append
with open('myfile.txt', mode='a') as f:
    f.write('\nthis is fourth line')

with open('myfile.txt', mode='r') as f:
    print(f.read())

# mode w - just read
with open('createMyfile.txt', mode='w') as f:
    f.write('I created this file')
