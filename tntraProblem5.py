#Problem 5 

def swapNumbers(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2 
    num1 = num1 - num2 
    return num1, num2

try: 
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Kindly enter valid numbers.")
else:

    num1, num2 = swapNumbers(num1, num2)

    print("After swapping")
    print("First number:", num1)
    print("Second number:", num2)