#all of the keys should be unique

always_true = True
while always_true:
    key = str(input("Enter the key of month:"))
    monthConversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "Octobor",
        "Nov": "November",
        "Dec": "December",

    }

    print(monthConversions.get(key , "Please enter a valid key"))

