#question 7
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

testEqual(is_even(100), True)
testEqual(is_even(37), False)
testEqual(is_even(0), True)