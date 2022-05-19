def charCounter(string1):
    newDict = {};
    for char in string1:
        if char in newDict:
            newDict[char] = newDict[char] + 1;
        else:
            newDict[char] = 1;
    return(newDict);

string2 = input("Enter a string :");
print(charCounter(string2));
