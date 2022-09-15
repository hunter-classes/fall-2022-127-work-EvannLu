from cmath import atan
from socket import BTPROTO_RFCOMM

#Q7
def is_even(n):
    if(n % 2 == 0):
        return True
    else:
        return False

print(is_even(10))
print(is_even(7))
print(is_even(0))

#Q8
def is_odd(n):
    if(n % 2 == 1):
        return True
    else:
        return False

print(is_odd(10))
print(is_odd(7))
print(is_odd(0))
      
#Q10-11
def is_rightangled(a, b, c):
    at= a**2
    bt = b**2
    ct = c**2
    
    if(at+bt==ct or bt+ct==at or ct+at==bt):
        return True
    else:
        return False

print(is_rightangled(5,12,13))
print(is_rightangled(3,4,6))