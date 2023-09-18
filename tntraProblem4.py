#Problem 4 

def stringsSwap(str1, str2):

    str1 = str1 + str2

    str2 = str1[:len(str1) - len(str2)]
    str1 = str1[len(str2):]

    return str1, str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ") 

string1, string2 = stringsSwap(string1, string2)

print("After swapping")
print("First String:", string1)
print("Second String:", string2)