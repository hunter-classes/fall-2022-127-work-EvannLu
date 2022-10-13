# Prompt 1: Write a function to find the smallest value in a listKfind smallest in a list of items.

import random

listKfind = []
for i in range(10):
    listKfind.append(random.randint(0, 1000))

print(listKfind)

def smallest(listKfind): 
    min = listKfind[0]
    for i in (listKfind):
        if min > i:
            min = i 
    return (min)

print(smallest(listKfind))

# Prompt 2: Write a function that returns a new list that contains all the odd items in the original list.

orgi = [5 , 6, 10, 25, 1432, 4906, 97, 107, 3245, 86]
newL = []

def listOdd(orgi):
    for i in orgi: 
        if i % 2 ==1:
            newL.append(i)
    return newL
print(listOdd(orgi))

# Prompt 3: Write a function that takes a string and returns a new string where all the words are capitalized.

low = "Computer Science takes alot of dedication to learn"
# no strings in list.
def capAll(l):
    return l.upper()

print(capAll(low))

# Prompt 4: Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case.

def longThan5(low):
# borrow low string from previous question 
    newS = []
    for i in low.split():
        if len(i) > 5: 
            newS.append(i.upper())
        else: 
            newS.append(i)
        sent = " ".join(newS)
    return sent

print(longThan5(low))

# Prompt 5: Write a function that takes a list of numbers and returns a new list with each item squared.




'''
Prompt 6: Write a function that takes two lists of numbers and returns a new list where each item is the 
corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
'''

