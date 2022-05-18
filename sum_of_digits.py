# write a program to find the sum of the digits of a number;

def getSum(number):
    sum = 0
    for n in str(number):
        sum += int(n)
    return sum


num = input("Enter a number to find sum of it's digits:")
print("Sum of digits is",getSum(num))
