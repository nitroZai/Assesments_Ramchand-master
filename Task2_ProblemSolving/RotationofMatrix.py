# First Transpose

arr = [[1,2,3],[4,5,6],[7,8,9]]

arrLen = len(arr)

for i in range(0,arrLen):
    for j in range(i+1, arrLen):
        temp = arr[i][j]
        arr[i][j] = arr[j][i]
        arr[j][i] = temp

# Second Interchanging the Column arrLen - j - 1

for i in range(0, arrLen):
    for j in range(0, arrLen//2):

        temp = arr[i][j]
        arr[i][j] = arr[i][arrLen-j-1]
        arr[i][arrLen - j -1] = temp

print("The Rotation of matrix is: {}".format(arr))

