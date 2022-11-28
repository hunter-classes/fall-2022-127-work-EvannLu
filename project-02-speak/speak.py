'''
Extras: 
1. Handle upper and lower case and/or punctuation. 
2. Have an option to translate different languages. 
3. Advanced translations like converting parts of words 
rather than straight substitutions or inserting pirate phrases.
'''

# read files 
p = open('pirate.dat')
rP = p.read()
sP = rP.split('\n')

l = open('input.txt')
rl = l.read().lower()
sl = rl.split()


# dict

dict = {}
for word in sP:
    ind = word.find(':')
    dict.update({word[0:ind]:word[ind+1:]})

# program
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

print(" ".join(nStory))





