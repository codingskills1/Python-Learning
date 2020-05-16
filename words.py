import sys
word = str(input("Enter the word(just word):"))
ask = str(input("Do you want to make it upper:")).lower()
if ask == "y" or ask == "yes":
    print(word.upper())
else:
    print(word.lower())
print("Enter quit for quit")
other = input(">>>>")
if other == "quit":
    sys.exit()

