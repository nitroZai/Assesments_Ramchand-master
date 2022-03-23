#Kadane's ALgorithm in 2D Form

arr = [[1,2,3],[4,5,1],[6,7,8]]

arrLen = len(arr)

sum = 0
max = 0
rowCoor = 0

for i in range(0, arrLen):
    for j in range(0, arrLen):

        sum = sum + arr[i][j]

    if(sum > max):
        max = sum
        rowCoor = i
    
    sum = 0

print(f"The wealth of the richest man in the community is {max} and he lives in Flat number {rowCoor+1}")