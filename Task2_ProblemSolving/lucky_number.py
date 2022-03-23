
#Minimum

matrix = [[3,7,8],[9,11,13],[15,16,17]]

dictCollect = {} 

for i in range(len(matrix)):
    dictCollect[min(matrix[i])] = 1
    
newmatrix = list(zip(*matrix))

for i in range(len(newmatrix)):
    if max(newmatrix[i]) in dictCollect:
        dictCollect[max(newmatrix[i])] += 1
    else:
        dictCollect[max(newmatrix[i])] = 1 
print(dictCollect)

for key, value in dictCollect.items():
    if value > 1:
        print(key)
