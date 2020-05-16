#list
import sys
friend1 = str(input("Enter your first friend: "))
friend2 = str(input("Enter your second friend: "))
friend3 = str(input("Enter your third friend: "))
friend4 = str(input("Enter your fourth friend: "))
main_list = [friend1,friend2,friend3,friend4]
print("here is list of your friends\n {}".format(main_list))
replace = str(input("Do you want to replace it: ")).lower().islower()
