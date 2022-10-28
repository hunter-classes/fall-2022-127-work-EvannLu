import random
from tkinter import NS

#lists for random input into the story
heroes = ['Napoleon', 'Shakespeare', 'Da Vinci', 'Htiler', 'Aristotle', 'Jesus', 'Lincoln']
nouns = ['cow', 'kitty', 'bird', 'rock', 'lion', 'cave', 'squirrel', 'fish', 'bear', 'zebra']
verbs = ['run', 'dance', 'slide', 'jump', 'think', 'stand', 'smile', 'listen', 'eat', 'kill', 'run', 'punch', 'duck', 'scream']
adjectives = ['attractive', 'dazzling', 'elegant', 'shapely', 'gorgeous', 'apathetic', 'resolute', 'honorable', 'unnatural', 'young', 'severe']
adverbs = ['abnormally', 'absentmindedly', 'accidentally', 'adventurously', 'anxiously', 'arrogantly', 'awkwardly', 'bashfully'] 

def madLibs(data): 
    textFile = open(data, "r+")
    storyData = textFile.read()
    nS = storyData.split()
    nStory = ''

    for i in range(len(nS)):

        if(nS[i] == "{hero}"):
            nStory += random.choice(heroes)

        elif(nS[i] == "{noun}"):
            nStory += random.choice(nouns)

        elif(nS[i] == "{verb}"):
            nStory += random.choice(verbs)

        elif(nS[i] == "{adjective}"):
            nStory += random.choice(adjectives)

        elif(nS[i] == "{adverb}"):
            nStory += random.choice(adverbs)

        else:
            nStory += nS[i]

        

    return nStory

print(madLibs("story.txt"))
