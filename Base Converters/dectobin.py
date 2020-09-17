import math
while True:
    try:
        decimal_number = int(input("enter a natural number in decimal (base 10): "))
    except ValueError:
        print("no.")
        continue
    if decimal_number <= 0:
        print("no.")
        continue
    else:
        break

binary_length = 1 + math.floor(math.log(decimal_number, 2))
binary_number = [0] * binary_length
for index, value in enumerate(binary_number):
    slot_value = 2 ** (binary_length - 1 - index)
    if (decimal_number - slot_value) >= 0:
        decimal_number -= slot_value
        binary_number[index] = 1
print("Equivalent number in binary (base 2): " + "".join(map(str, binary_number)))
