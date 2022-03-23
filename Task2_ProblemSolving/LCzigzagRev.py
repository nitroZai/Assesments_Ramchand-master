

mat = [[1,2,3],[4,5,6],[7,8,9]]

diction = {} 

row = len(mat)
col = len(mat[0])

for i in range(row):
    for j in range(col):

        if i+j in diction:
            diction[i+j].append(mat[i][j])
        else:
            diction[i+j] = [mat[i][j]]
        
#print(diction)

aR = []
dictLen = len(diction)

boox = False

for key in diction:
    #for i in range(dictLen):
    tempList = diction[key]
    tempLen = len(tempList)
    if boox == False:

        for i in range(tempLen-1, -1, -1):
            aR.append(tempList[i])
        boox = True
    else:

        for i in range(tempLen):
            aR.append(tempList[i])
        boox = False

print(aR)