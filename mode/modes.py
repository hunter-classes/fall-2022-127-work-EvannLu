def findLargest(l):
    largeSoFar = l[0]
    for item in l[1:]:
        if item > largeSoFar: 
            largeSoFar = item 
    return largeSoFar

def freq(l,v):
    count = 0 
    for item in l:
        if item == v: 
            count+=1
    return count



'''
classwork: create mode

Strategy:
- assue the first value is the mode 
- we can grab its frequency 

for each remaining item in the dataset" 
    count that items frequence and see if
    it's the new mode so far

'''

def mode(l): 
    modeSoFar = l[0]
    freqSoFar = freq(l,modeSoFar)
    for i in l: 
        if freq(l,i) > freqSoFar:
            modeSoFar = i 
            freqSoFar = freq (l,i)
    return modeSoFar

import random

def buildRandomList(s,m):#size/max value
    l = []
    i = 0
    while i != s:
        l.append(random.randint(1,m))
        i+=1
    return l
def testMode(s,max):
    l = buildRandomList(s,max)
    m = mode(l)
    print(m)
    return m


list = [23, 53, 65, 17, 9, 250, 100, 23]
print(findLargest(list))
print(freq(list, 23))
print(mode(list))
print(buildRandomList(10,20))
print(testMode(20,10))
















