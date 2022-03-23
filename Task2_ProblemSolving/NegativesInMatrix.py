

arr = [[1,-2,-3,-1],[2,3,4,-1],[1,2,-1,-1]]

m = len(arr)
n = len(arr[0])
count= 0

for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1,-1):
        if arr[i][j] < 0:
            count = count + 1

print(f"The number of negatives in the Matrix {arr} are {count}")