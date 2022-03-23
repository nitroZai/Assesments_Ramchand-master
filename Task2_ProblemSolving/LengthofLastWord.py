# Find the length of the last word of the String


s = "Hello WOrld, Good Morning"

sLen = len(s)

count = 0

for i in range(sLen - 1, -1, -1):

    if s[i] != ' ':
        count = count + 1
    elif count > 0:
        break


print("The length of the last word of the sentence is {}".format(count))