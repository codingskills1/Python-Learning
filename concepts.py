always_true = True
while always_true:
    row = int(input("Enter the row number: "))
    column = int(input("Enter the column number: "))
    multi_lists = [
        [1,2,3,4],
        [5,6,7,8],
        [9,0]
        ]
    print(multi_lists[row][column])
