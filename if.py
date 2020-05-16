always_true = True
while always_true:
    from math import*
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    number3 = int(input("Enter third number:"))
    def max(num1,num2,num3):
        if num1 > num2 and num1> num3:
            print("the greatest number is {}".format(num1))
        elif num2 > num1 and num2 > num3:
            print("the greatest number is {}".format(num2))
        elif num3 >num1 and num3 > num2:
            print("the greatest number is {}".format(num3))
        elif num1 == num2 and num2 == num3:
            print("Please change your numbers they are same")
            

    max(number1,number2,number3)
