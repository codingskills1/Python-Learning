print("""
        l           ll         l       llllllll        ll              llllllllll      lllllllll        ll           ll
          l        l  l       l        ll              ll              l               l       l       l  l        l   l
            l     l     l    l         llllllll        ll              l               l       l     l      l     l      l
              l  l       l  l          ll              ll              llllllllll      lllllllll   l          l  l         l
                l          l           llllllll        llllllllll                                l              l            l   """)
n1 = input("Enter the first word(or number):")
n2 = input("Enter the second word(or number):")
n3 = input("Enter the third word(or number):")
n4 = input("Enter the fourth word(or number):")
main_list = [n1,n2,n3,n4]
print("here is your list:{}".format(main_list))
print("Enter 'help'  for more information")
while True:
    user = input(">>>>").lower()
    if user == "help":
        print(
"Enter  'remove' for removing something \n"
"Enter  'append' for appending someitems \n"
"Enter  'insert' for inserting something \n"
"Enter  '  pop 'for removing the last item\n"
"Enter  'sort  'for sorting the list\n"
"Enter  'reverse'for reversing the list\n"
"Enter  'change' for changing Items ")
    elif user == "remove":
        item = input("Enter the item do you want to remove:")
        x = main_list.remove(item)
        print("target item removed")
        print(main_list)
    elif user == "append":
        add = input("Enter the item that you want to append to your list:")
        print("answer:{}".format(main_list.append(add)))
        print("target item appended")
        print(main_list)
    elif user == "insert":
        place = int(input("Enter the index of that:"))
        main = int(input("Enter the main number(in this option just number): "))
        h = main_list.insert(place,main)
        print(main_list)
    elif user == "extend":
        print("in this part you are supposed to Enter another list:")
        first = input("Enter the first word of list:")
        second = input("Enter the second word of list:")
        third = input("Enter the third word of list:")
        fourth = input("Enter the fourth word of list:")
        index = [first,second,third,fourth]
        print("here is your list {}".format(index))
        the_main = main_list.extend(index)
        print("done")
    elif user == "pop":
        last = main_list.pop()
        print(main_list)
    elif user == "sort":
        main_list.sort()
        print(main_list)
    elif user == "reverse":
        main_list.reverse()
        print(main_list)
    elif user == "index":
        checking = input("Enter the Item")
        check = main_list.index("checking")
    elif user == "copy":
        mainlist2 = main_list.copy()
        print("here is a copy of your original list {}".format(mainlist2))
    elif user == "change":
        main_word = int(input("Enter the main word that you want to change it:"))
        new = int(input("Enter the new Item:"))
        main_list[main_word]=new
        print(main_list)










