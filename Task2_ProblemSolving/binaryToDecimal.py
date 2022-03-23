import math

binaryString = "10101"

decimalNum = 0
powVar = 0
for x in binaryString:
    if x == '1':
        decimalNum += math.pow(2, powVar)
    
    powVar += 1

print(decimalNum)