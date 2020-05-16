import sys
try:
    name = str(input("Enter that name:"))
    replace = str(input("Enter the main letter:"))
    replace_with = str(input("Enter the letter that you want to replace with:"))
    y = name.replace(replace,replace_with)
    print("write exit for exiting")
    print(y)
except ValueError:
    print("this value is not defined")
except KeyboardInterrupt:
    print("if you want to exit write exit")
x = str(input(">>>>")).lower()
if x == "exit":
    sys.exit()
