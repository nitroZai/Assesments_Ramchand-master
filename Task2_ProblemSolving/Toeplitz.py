# Create a matrix whose every diagonal elmeents are same


arr = [[1,1,1,4],[1,1,1,1],[4,1,1,1]]

m = len(arr)
n = len(arr[0])

for x in range(0, m - 1):
    for y in range(0, n - 1):

        if arr[x+1][y+1] != arr[x][y]:
            print("This ins't a Toeplitz Matrix")
            break