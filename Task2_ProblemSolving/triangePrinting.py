
upto = 10

strHelp = ""

for x in range(1, upto):

    for y in range(1, x+1):

        strHelp += str(y) + " "

    print(strHelp)
    strHelp = ""