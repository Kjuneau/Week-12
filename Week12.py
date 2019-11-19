#   Week-12
#   Kevin Juneau
#   CSCI 102 - Section B
#   Week 11 - Part A

def PrintOutput(string):
    string = str(string)
    print('OUTPUT',string)

def LoadFile(filename):
    f = open(filename)
    file = f.readlines()
    for x in file:
        file[file.index(x)] = x.rstrip('\n\r ')
    return file
