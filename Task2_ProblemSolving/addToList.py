

arr = [1,0,0,8]
k = 90000

arrLen = len(arr)

string = ""

for i in range(0, arrLen):
    string = string + str(arr[i])

inte = int(string)

sum = inte + k

arr = []

while sum > 0:
    temp = sum % 10
    sum = sum // 10
    arr.append(temp)
    print(temp)

arrLen = len(arr)


i = 0
j = arrLen - 1

while i <= j:

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    i += 1
    j -= 1

print(arr)



# temp = k
# for i in range(arrLen - 1, -1, -1):

#     x = temp % 10
#     temp = temp// 10
#     sum = (arr[i] + x)
#     if sum > 9:
#         y = sum
#         j = i
#         while y > 0:
#             t = y%10
#             y = y//10
#             arr[j] += t
#             j -= 1
#     else:
#         arr[i] = sum

# print(arr)
