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



list = [23, 53, 65, 17, 9, 250, 100, 23]
print(findLargest(list))
print(freq(list, 23))