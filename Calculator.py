try:
    while True:
        from math import*
        import sys
        print("Welcome to MHG Calculator(write'help' for help)")
        user = input(">>>>>")
        if user == "help":
            print(
        "Enter'add' for addition\n Enter 'sub'for subtraction\n Enter 'multi' for multipiulation"
        "Enter ceil for ceil \n Enter floor for floor \n Enter max for max \n Enter min for min"
        "Enter power for power \n Enter round for rounding \n Enter sqrt for squaring\n Enter abs for absolute number")
        elif user == "add":
            num1 = int(input("First number:"))
            num2 = int(input("Second number:"))
            result = num1 + num2
            print("answer:{}".format(result))
        elif user == "sub":
            num1 = int(input("First number:"))
            num2 = int(input("Second number:"))
            result = num1 - num2
            print("answer:{}".format(result))
        elif user == "multi":
            num1 = int(input("First number:"))
            num2 = int(input("Second number:"))
            result = num1 * num2
            print("answer:{}".format(result))
        elif user == "floor":
            num1 = float(input("number:"))
            print("answer:{}".format(floor(num1)))
        elif user == "max":
            num1 = int(input("First number:"))
            num2 = int(input("Second number:"))
            result = max(num1,num2)
            print("number {} is greater".format(result))
        elif user == "min":
            num1 = int(input("First number:"))
            num2 = int(input("Second number:"))
            result = min(num1,num2)
            print("number {} than the other one".format(result))
        elif user == "round":
            num1 = float(input("number:"))
            print("answer:{}".format(round(num1)))
        elif user == "sqrt":
            num1 = float(input("number:"))
            print("answer:{}".format(sqrt(num1)))
        elif user == "abs":
            num1 = int(input("number:"))
            print("answer:{}".format(abs(num1)))
        elif user == "ceil":
            num1 = float(input("number:"))
            print("answer:{}".format(ceil(num1)))
        elif user == "power":
            num1 = int(input("Enter the main number:"))
            num2 = int(input("Enter the power of your main number:"))
            print("answer:{}".format(pow(num1,num2)))
        elif user == "quit":
            sys.exit()
except ValueError:
    print("this value is not defined enter help for more informations")
except KeyboardInterrupt:
    print("Enter quit if you want to exit if not enter help for more informations")





