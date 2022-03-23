	
matrix = [[1,2,3],[4,5,6],[7,8,9]]

m = len(matrix)
n = len(matrix[0])
topbound = 0
leftbound = 0
rightbound = n-1
bottombound = m-1

ans = []
while len(ans) < m*n:
    #From the top, travel from left to right
    if topbound <= bottombound:
        for i in range(leftbound, rightbound+1):
            ans.append(matrix[topbound][i])
        topbound+=1
        
    #From the right, travel from top to bottom
    if leftbound <= rightbound:
        for i in range(topbound, bottombound+1):
            ans.append(matrix[i][rightbound])
        rightbound-=1

    #From the bottom, travel from right to left
    if topbound <= bottombound:
        for i in range(rightbound, leftbound-1, -1):
            ans.append(matrix[bottombound][i])
        bottombound-=1

    #From the left, travel from bottom to top
    if leftbound <= rightbound:
        for i in range(bottombound, topbound-1, -1):
            ans.append(matrix[i][leftbound])
        leftbound +=1


print(ans)