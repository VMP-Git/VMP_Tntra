def stringPalindrome(string):

    stringClean = ' '.join(string.split()).lower()

    return stringClean == stringClean[::-1]

inputString = input("Enter a string: ")

if stringPalindrome(inputString):
    print("It is palindrome")
else:
    print("It is not a palindrome") 