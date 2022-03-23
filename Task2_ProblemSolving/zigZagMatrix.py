arr = [[1,2,3],[4,5,6],[7,8,9]]
n = len(arr)

diction = {}

for i in range(n):
    for j in range(n):

        if i-j in diction:
            diction[i-j].append(arr[i][j])
        else:
            diction[i-j] = [arr[i][j]]


sortie = sorted(diction.items(), reverse=True)
print(sortie)

boo = True
aR = []

for key, value in sortie:
    tempList = list(value)
    if boo == True:
        for i in range(len(tempList)):
            aR.append(tempList[i])
        boo = False
    elif boo == False:
        for i in range(len(tempList)-1,-1,-1):
            aR.append(tempList[i])
        boo = True

print(aR)


# # # # # diction = {1:"2", 0:"0", -1:"1"}
# # # # # print(sorted(diction.items()))    

# # # from ast import operator
# # # from audioop import reverse


# # # diction = { 2: [1], 1: [1,2], 0: [3,4,5], -1:[5,6], -2:[8]}

# # # sortedDict = sorted(diction.keys(), reverse = True)

# # # ar = []

# # # n = 3
# # # matLen = 9
# # # dictLen = len(diction)
# # # print(dictLen)

# # # boo = True

# # # aDiction = list(diction.keys())

# # # tLen = 0

# # # for key in aDiction:
# # #     for i in range(dictLen):
        
# # #         if key <= 0:
# # #             tLen = key + n
# # #         else:
# # #             tlen = n - key

# # #         if boo == True:
# # #             for j in range(tLen):
                
# # #                 ar.append(diction[key].pop(0))
            
# # #             boo = False
        
# # #         else:
# # #             temp = diction[key].reverse()
# # #             for j in range(tLen):

# # #                 ar.append(diction[key].pop(0))
            
# # #             boo = True


# # # print(ar)


