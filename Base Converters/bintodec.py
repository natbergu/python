while True:
    no = False
    try:
        num = int(input("Enter an unsigned binary (base 2) number: "))
    except ValueError:
        print("no.")
        continue
    if num < 0:
        print("no.")
        continue
    else:
        for digit in str(num):
            if int(digit) > 1 and no == False:
                print("no.")
                no = True
        if no == False:
            break
        else:
            continue
bin = [int(x) for x in str(num)]
dec = 0
for idx, val in enumerate(bin):
    dec += val * 2 ** (len(bin) - 1 - idx)
print("Equivalent number in decimal (base 10): " + str(dec))
