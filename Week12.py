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

def UpdateString(string1,string2,index):
    new_string = ''
    for x in range(len(string1)):
        if x == index:
            new_string += string2
        elif x != index:
            new_string += string1[x]
    return new_string
