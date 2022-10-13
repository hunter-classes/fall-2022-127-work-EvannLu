# Prompt 1: Write a function to find the smallest value in a listKfind smallest in a list of items.

from itertools import count
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

numlib = [3,4,5]

def squareL(numlib):
    updateL = []
    for i in numlib: 
        updateL.append(i**2)
    return updateL 

print(squareL(numlib))

'''
Prompt 6: Write a function that takes two lists of numbers and returns a new list where each item is the 
corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
'''

L1 = [1, 2, 3]
L2 = [10, 20, 30]

def combineNum(L1, L2):
    sumList=[]
    index = 0
    for i in L1 and L2: 
        sumList.append(L1[index] + L2[index])
        index +=1 
    return sumList 

print(combineNum(L1,L2)) 


# Chap 10, Q#10: Count how many words in a list have length 5.

wList = ['Hello', 'Hi', 'Pineapples', 'code', 'win', 'eight']

def countWords(lst):
    count = 0
    for i in lst:
        if len(i) == 5: 
            count = count + 1
    return count 

print(countWords(wList))

# Chap 10, Q#11: Sum all the elements in a list up to but not including the first even number.

def sum(lst):
    sum = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum = sum + lst[index]
        index = index + 1
    return sum

lst = []
for i in range(100):
    lst.append(random.randint(0,1000))

print(sum(lst))

# Chap 10, Q#12: Count how many words occur in a list up to and including the first occurrence of the word “sam”.

listWord = ['dude', 'hi', 'jeep', 'hippy', 'sam', 'les']

def sam(l):
    count = 0
    i = 0
    while l[i].lower() != 'sam' and i < len(l): 
        count += 1
        i += 1
    return count + 1

print(sam(listWord))