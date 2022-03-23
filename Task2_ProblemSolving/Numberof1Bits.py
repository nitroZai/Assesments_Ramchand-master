binInt = 11010
count = 0

while binInt != 0:

    if (binInt % 2) == 1:
        count = count + 1
        print(binInt)
        binInt >> 1

print(count)

