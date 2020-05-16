import sys
number = int(input("Enter the number(0,1,2) "))
fruits = ["apple","banana","cherry"]
print(fruits[number])
do = input("do you want us to show list for you? ").lower
if do == "y" or "yes":
    print("here is the list \n {}".format(fruits))
elif do == "n" or "no":
    sys.exit()
