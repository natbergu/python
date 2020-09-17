import math
print("binary counting")
while True:
    try:
        limit = int(input("choose digit limit > "))
    except ValueError:
        print("no.")
        continue
    if limit <= 0:
        print("no.")
        continue
    else:
        break

count = 0
print(0)
while count < (2 ** limit - 1):
    count += 1
    calculation_number = count
    binary_length = 1 + math.floor(math.log(calculation_number,2))
    binary_number = [0] * binary_length
    for index, value in enumerate(binary_number):
        slot_value = 2 ** (binary_length - 1 - index)
        if (calculation_number - slot_value) >= 0:
            calculation_number -= slot_value
            binary_number[index] = 1
    print("".join(map(str, binary_number)))
