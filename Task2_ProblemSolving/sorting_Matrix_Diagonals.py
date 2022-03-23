
diction = {}

mat = [[1,2,1,2],[1,2,3,4],[1,2,1,1]]

row = len(mat)
col = len(mat[0])

for i in range(row):
    for j in range(col):

        if (i-j) in diction:
            diction[i-j].append(mat[i][j])
        else:
            diction[i-j] = [mat[i][j]]

print(diction.items())

for keys in diction.keys():

    dList = diction[keys]

    for i in range(len(dList)):
        for j in range(len(dList)):

            if dList[i] < dList[j]:
                temp = dList[i]
                dList[i] = dList[j]
                dList[j] = temp
    
    diction[keys] = dList

for i in range(row):
    for j in range(col):
        
        mat[i][j] = diction[i-j].pop(0)

print(mat)


print(diction.items())
