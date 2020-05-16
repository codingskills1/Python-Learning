import sys
def setapp():
    print("Welcome to set application")
    th1 = input("Enter first word(or number): ")
    th2 = input("Enter second word(or number): ")
    th3 = input("Enter third word(or number): ")
    th4 = input("Enter fourth word(or number): ")
    make_set = {th1,th2,th3,th4}
    print("here is your set {}".format(make_set))
    print("Enter help for more information")
    x = True
    while x:
        user = input(">>>>").lower()
        if user == "help":
            print(""
        "Enter discard/remove for removing Item \n"
        "Enter add to add Item to your set \n")
        elif user == "discard" or user == "remove":
            Item_remove = input("Enter the Item that you want to remove: ")
            remove = make_set.discard(Item_remove)
            print("done")
            print(make_set)
        elif user == "add":
           add = input("Enter the Item that you want to add to your set:")
           make_set.add(add)
           print(make_set)
        elif user == "union" or user == "update":
            print("for extending another set to your set you need to make a new one!!!")
            thi1 = input("Enter first word(or number): ")
            thi2 = input("Enter second word(or number): ")
            thi3 = input("Enter third word(or number): ")
            thi4 = input("Enter fourth word(or number): ")
            make_set1 = {thi1, thi2, thi3, thi4}
            make_new_set = make_set.union(make_set1)
            print("this is your extended set {}".format(make_new_set))
        elif user == "quit":
            sys.exit()
use = input("set-app,list-app(choose one of them):")
if use == "set-app":
    setapp()




