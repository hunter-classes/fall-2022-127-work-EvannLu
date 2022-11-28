'''
Extras: 
1. Handle upper and lower case and/or punctuation. 
2. Another language translation. 
2. Advanced translations like converting parts of words 
rather than straight substitutions or inserting pirate phrases.
'''

# read files 
p = open('pirate.dat')
rP = p.read()
sP = rP.split('\n')

r = open('randlang.dat')
rR = r.read()
sR = rR.split('\n')

l = open('input.txt')
rl = l.read().lower()
sl = rl.split()


# two dictionaries
dictF = {}
for word in sP:
    ind = word.find(':')
    dictF.update({word[0:ind]:word[ind+1:]})

dictS = {}
for word in sR: 
    ind = word.find(':')
    dictS.update({word[0:ind]:word[ind+1:]})

# program
def dictionary(dict): 
    nStory = []
    i = 0 
    for word in sl: 
        if word in dict.keys(): 
            nStory.append(dict[word])
        else:
            nStory.append(word)
        if nStory[i] == nStory[0]:
            nStory[i] = nStory[i].capitalize()
        elif "." in nStory[i - 1]:
            nStory[i] = nStory[i].capitalize()
        elif "?" in nStory[i - 1]:
            nStory[i] = nStory[i].capitalize()
        elif "!" in nStory[i - 1]:
            nStory[i] = nStory[i].capitalize()
    i = i + 1    
    return " ".join(nStory)

print("First Translation:" + '\n' + dictionary(dictF) + '\n')
print("Second Translation:" + '\n' + dictionary(dictS))





