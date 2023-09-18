#Problem 3 

def minMaxvalue(arr):
    if len(arr) == 0:
        return None, None
    
    minValue = arr[0]
    maxValue = arr[0]

    for x in arr:
        if x < minValue:
            minValue = x
        elif x > maxValue:
            maxValue = x

    return minValue, maxValue

try: 
    inputString = input("Enter an array on numbers seperated by spaces: ")
    inputArray = [float(x) for x in inputString.split()]
except ValueError:
    print("Invalid input. Kindly enter a valid array of numbers")
else:
    minValue, maxValue = minMaxvalue(inputArray)

    if minValue is not None and maxValue is not None:
        print("Minimum is", minValue)
        print("Maximum is", maxValue)