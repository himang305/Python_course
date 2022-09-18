from math import *

def calculateArea(radius):
    area = pi * pow(radius,2)

    return area

r = 2
x = calculateArea(r)
print(x)
u = 5
j = calculateArea(u)
print(j)

print(len("Hello World"))

def customLen(s):
    count = 0
    for ch in s:
        count += 1
    return count

simpleString = "Hello World"
y = customLen(simpleString)
print(y)




# GCDFunction File

# Return the gcd of two integers
def gcd(n1, n2):
    gcd = 1 # Initial gcd is 1
    k = 2 # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # update gcd
        k += 1

    return gcd # Return gcd



#  Import GCD   
from GCDFunction import gcd # Import the gcd function

# Prompt the user to enter two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for", n1,
      "and", n2, "is", gcd(n1, n2))

