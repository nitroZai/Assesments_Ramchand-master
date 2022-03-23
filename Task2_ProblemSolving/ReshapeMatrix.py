

from numpy import reshape


r = 2
c = 4

arr = [[1,2,3,5],[12,5,6,3],[9,0,8,7]]

m = len(arr)
n = len(arr[0])

reShape = []

count = 0

dummy1D = []
for i in range( 0, m ):
    for j in range( 0, n):
        dummy1D.append(arr[i][j])

for i in range(0, r):
    temp = []
    for j in range(  0, c):
        temp.append(dummy1D[count])
        count = count + 1
    
    reShape.append(temp)

print(f"Previous Matrix: {arr} ReShape matrix {reShape}")