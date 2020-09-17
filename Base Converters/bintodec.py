while True:
    no = False
    try:
        number = int(input("Enter an unsigned binary (base 2) number: "))
    except ValueError:
        print("no.")
        continue
    if number < 0:
        print("no.")
        continue
    else:
        for digit in str(number):
            if int(digit) > 1 and no == False:
                print("no.")
                no = True
        if no == False:
            break
        else:
            continue

binary_number = [int(x) for x in str(number)]
decimal_number = 0
for index, value in enumerate(binary_number):
    decimal_number += value * 2 ** (len(binary_number) - 1 - index)
print("Equivalent number in decimal (base 10): " + str(decimal_number))
