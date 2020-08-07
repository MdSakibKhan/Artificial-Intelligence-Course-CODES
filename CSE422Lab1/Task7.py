import math

bornYear = 1980

for i in range(0, int(math.sqrt(bornYear) + math.sqrt(bornYear))): # taken the range within Square Root, as it should not exceed this Range
    if i**2 - i == bornYear:
        print("X =", i)
        break
