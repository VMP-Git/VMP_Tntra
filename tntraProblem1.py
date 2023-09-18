def count_occurances(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count

inputString = input("Enter a string: ")
inputCharacter = input("Enter a character to count: ")

result = count_occurances(inputString, inputCharacter)

print("Output: ", result)
#print("The character", inputCharacter, "apperes", "'",  result, "'",  "time in the string", "'" ,inputString, "'" )