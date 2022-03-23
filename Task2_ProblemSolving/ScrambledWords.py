
def swap(string, x, y):
    while x <= y:

        if (string [x] == "!" or string [x] == "," or string [x] == "." or string [x] == "?" or string [x] == ";"):
            x += 1
            y -= 1
            continue
        elif ((string [y] == "!" or string [y] == "," or string [y] == "." or string [y] == "?" or string [y] == ";")):
            x += 1
            y -= 1
            continue

        temp = string[x]
        string[x] = string[y]
        string[y] = temp
        x += 1
        y -= 1

s = input("Enter the String that you'd like to scamble")
stLen = len(s) - 1
st = list(s)

i = 0
j = 0

while j != stLen + 1:
    if st[j] == " ":
        x = i + 1
        y = j - 2

        if j - i < 2:
            continue

        for z in range (y+1, -1, -1):
            if (st [z] == "!" or st [z] == "," or st [z] == "." or st [z] == "?" or st [z] == ";"):
                y -= 1
                #print(y)
            else:
                break

        swap(st, x, y)

        i = j + 1           

    j += 1

    if j == stLen:
        
        x = i + 1
        y = j - 1
        
        for z in range (y+1, -1, -1):
            if (st [z] == "!" or st [z] == "," or st [z] == "." or st [z] == "?" or st [z] == ";"):
                y -= 1
                #print(y)
            else:
                break

        swap(st, x, y)

retStr = ""

for x in st:
    retStr = retStr + x

print(retStr)