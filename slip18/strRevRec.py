# Q2.Write python program to accept and print string in reverse order using recursion.

def reverseString(string):
    if len(string) == 0:
        return
    temp = string[0]
    reverseString(string[1::])
    print(temp, end='')

newStr = "Geeks for Geeks";
reverseString(newStr)
