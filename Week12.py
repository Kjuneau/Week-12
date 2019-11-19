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
    PrintOutput(new_string)

def FindWordCount(List,String):
    n = 0
    for x in List:
        n += x.count(String)
    return n

def ScoreFinder(player_names,player_scores,player):
    score = ''
    for x in player_names:
        if x.lower() == player.lower():
            score = player_scores[player_names.index(x)]
    if score == '':
        PrintOutput('player not found')
    else:
        PrintOutput((player_names[player_scores.index(score)]+' got a score of '+str(score)))

def Union(l1,l2):
    l3 = l1 + l2
    for x in l3:
        while l3.count(x) > 1:
            l3.remove(x)
    return l3

def Intersection(l1,l2):
    l3 = []
    for x in l1:
        if x in l2:
            l3.append(x)
    return l3

def NotIn(l1,l2):
    l3 = []
    for x in l1:
        if x not in l2:
            l3.append(x)
    return l3
