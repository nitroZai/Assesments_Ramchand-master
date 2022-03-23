
arr = [1,2,3,4,5,6,7,8,9]

arrLen = len(arr)

r = 3
c = 3

newShape = []

count = 0
for i in range(0, r):
    temp = []
    for j in range( 0, c):
        temp.append(arr[count])
        count = count + 1

    newShape.append(temp)


print(f"The previous array is {arr} The Re Shaped Array is: {newShape}")