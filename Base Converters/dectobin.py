import math
while True:
    try:
        num = int(input("enter a natural number in decimal (base 10): "))
    except ValueError:
        print("no.")
        continue
    if num <= 0:
        print("no.")
        continue
    else:
        break
num = int(num)
binl = 1 + math.floor(math.log(num,2))
bin = [0] * binl
for idx, val in enumerate(bin):
    slotval = 2**(binl-1-idx)
    if (num - slotval) >= 0:
        num -= slotval
        bin[idx] = 1
print("Equivalent number in binary (base 2): " + "".join(map(str, bin)))
