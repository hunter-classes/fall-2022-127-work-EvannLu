def madlibs(file):
    retStr = ""
    t = 0
    NOUNS=["banana","cookie","Mcdonalds","Burger King","cupcake","school","man","day","people","teacher","student","thing"]
    VERBS=["ate","walked","slept","jumped","ran","destroyed","slowed","play","relax","want","look","use","work","start","try","ask","need","talk"]
    hero = random.choice(["Daniel","Cookie Monster","Anna","Mandy","The Queen","Nub","Pye","Captain","Spagett"])

    f = open(file, "r")
    str = f.read()
    while (t < len(str)):
        if (str[t:t + 6] == "<VERB>"):
            retStr += VERBS[random.randint(0,len(VERBS)-1)]
            t+=6
        elif (str[t:t + 6] == "<HERO>"):
            retStr += hero
            t+=6
        elif (str[t:t + 6] == "<NOUN>"):
            retStr += NOUNS[random.randint(0, len(NOUNS)-1)]
            t+=6
        else:
            retStr += str[t]
            t+=1
    return retStr

print("File: "  + open("textFile.txt","r").read() + "\n")
print("After madlibs: " + madlibs("textFile.txt"))





