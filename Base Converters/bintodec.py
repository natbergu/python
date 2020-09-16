num = input("Enter an unsigned binary (base 2) number: ")
bin = [int(x) for x in str(num)]
dec = 0
for idx, val in enumerate(bin):
    dec += val * 2 ** (len(bin) - 1 - idx)
print("Equivalent number in decimal (base 10): " + str(dec))
