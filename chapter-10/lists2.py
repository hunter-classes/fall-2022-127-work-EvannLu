# Exercise 4

def average(numlist):

    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)

numlist = [1,234,456,87,3,90,34]
print(average(numlist))


# Exercise 6

list = [2, 3, 4]
def sum_of_squares(xs):
    sum = 0
    for number in xs:
        sum = sum + (number * number) 
    
    return sum

print(sum_of_squares(list))