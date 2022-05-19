from math import factorial

n = int(input("Enter a number:"))

def facto(num):
    return factorial(num)
print("Factorial of ",n,"is", facto(n))
