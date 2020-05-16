from math import*
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
def maximum(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num1 == num2 and num2 == num3:
        print("equal")
    else:
        return num3
print(maximum(number1,number2,number3))


