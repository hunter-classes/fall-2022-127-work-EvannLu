# Exercise 5
def max(big):
    max = 0
    for e in big:
        if e > max:
            max = e
    return max
big = [9, 57, 80, 12]

print(max(big))


# Exercise 7
import random 

numlib = []
for i in range(100):
    numlib.append(random.randint(0, 1000))

print(numlib)


def countOdd(numlib):
    odd = 0
    for i in numlib: 
        if i % 2 !=0:
            odd = odd + 1
    return odd

oddNum = str(countOdd(numlib))
print("There are " + oddNum + " odd numbers in this list.")

#Exercise 8
import random 

evenlib = []
for i in range(100): 
    evenlib.append(random.randrange(-100, 100))

print(evenlib)


def sumNeg(evenlib):
    sum = 0 
    for i in evenlib:
        if i > 0:
            sum = sum + i 
    return sum 

print(sumNeg(evenlib))