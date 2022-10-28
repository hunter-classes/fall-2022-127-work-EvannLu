import random

heroes = ['Napoleon', 'Shakespeare', 'Da Vinci', 'Htiler', 'Aristotle', 'Jesus', 'Lincoln']
nouns = ['cow', 'kitty', 'secretary', 'rock', 'lion', 'cave', 'zookeeper', 'fish', 'bear', 'zebra']
verbs = ['run', 'dance', 'slide', 'jump', 'think', 'stand', 'smile', 'listen', 'eat', 'kill', 'run', 'punch', 'duck', 'scream']
adjectives = ['attractive', 'dazzling', 'elegant', 'shapely', 'gorgeous', 'apathetic', 'resolute', 'honorable', 'unnatural', 'young', 'severe']
adverbs = ['abnormally', 'absentmindedly', 'accidentally', 'adventurously', 'anxiously', 'arrogantly', 'awkwardly', 'bashfully']
heroes = random.choice(heroes)

def madlibs(file):
    retStr = ""
    t = 0

    heroes = ['Napoleon', 'Shakespeare', 'Da Vinci', 'Htiler', 'Aristotle', 'Jesus', 'Lincoln']
    nouns = ['cow', 'kitty', 'secretary', 'rock', 'lion', 'cave', 'zookeeper', 'fish', 'bear', 'zebra']
    verbs = ['run', 'dance', 'slide', 'jump', 'think', 'stand', 'smile', 'listen', 'eat', 'kill', 'run', 'punch', 'duck', 'scream']
    adjectives = ['attractive', 'dazzling', 'elegant', 'shapely', 'gorgeous', 'apathetic', 'resolute', 'honorable', 'unnatural', 'young', 'severe']
    adverbs = ['abnormally', 'absentmindedly', 'accidentally', 'adventurously', 'anxiously', 'arrogantly', 'awkwardly', 'bashfully']
    heroes = random.choice(heroes)


    f = open(file, "r")
    str = f.read()
    while (t < len(str)):
        if (str[t:t + 6] == "{verb}"):
            retStr += verbs[random.randint(0,len(verbs)-1)]
            t+=6
        elif (str[t:t + 6] == "{hero}"):
            retStr += heroes
            t+=6
        elif (str[t:t + 6] == "{noun}"):
            retStr += nouns[random.randint(0, len(nouns)-1)]
            t+=6
        else:
            retStr += str[t]
            t+=1
    return retStr

print("File: "  + open("story.txt","r").read() + "\n")
print("After madlibs: " + madlibs("story.txt"))