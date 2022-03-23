mat = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

diction = {}

matLen = len(mat)
smallboxLen = len(mat)//3

p = 0

for i in range(0, matLen):
    for j in range(0, matLen):
        
        var = mat[i][j]

        if var == ".":
            continue

        if var in diction:
            diction[var] += 1
        else:
            diction[var] = 1
        
        if diction[var] > 1:
            print("Isn't a valid Sudoku!")
    
    diction = {}


for i in range(0, matLen):
    for j in range(0, matLen):
        
        var = mat[j][i]

        if var == ".":
            continue

        if var in diction:
            diction[var] += 1
        else:
            diction[var] = 1
        
        if diction[var] > 1:
            print("Isn't a valid Sudoku!")

    diction = {}

for i in range(0, 3):
    for j in range(0, matLen, 3):
        for x in range(p, (i+1)*3):
            for y in range(j, j+3):

                var = mat[x][y]

                if var == ".": continue
                
                if var in diction:
                    diction[var] += 1
                else:
                    diction[var] = 1
                
                if diction[var] > 1:
                    print("The Matrix isn't a valid Sudoku!")
                    break
        print(diction)
        diction = {}
    p = p+3

print("The matrix is a valid sudoku!")
                

