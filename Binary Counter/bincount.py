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
overnum = 0
binlen = 0
binnum = []
print(0)
while overnum < (2 ** limit - 1):
    overnum += 1
    calcnum = overnum
    binlen = 1 + math.floor(math.log(calcnum,2))
    binnum = [0] * binlen
    for idx, val in enumerate(binnum):
        slotval = 2 ** (binlen - 1 - idx)
        if (calcnum - slotval) >= 0:
            calcnum -= slotval
            binnum[idx] = 1
    print("".join(map(str, binnum)))
