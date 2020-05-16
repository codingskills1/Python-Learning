# Exponent Function
main_num = int(input("Enter the main number: "))
power_num = int(input("Enter the power of your number: "))
def raise_in_power(main , power):
    result = 1
    for index in range(power):
        result = result * main
    return result
print(raise_in_power(main_num , power_num))


