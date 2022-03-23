
binaryList = []
num = 16

while num >= 1:

    if num % 2 == 0:
        binaryList.append(0)
    else:
        binaryList.append(1)

    num = num/2

binaryList.reverse()

print(binaryList)