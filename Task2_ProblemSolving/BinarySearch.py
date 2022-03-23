


# Binary Search on the Array


arr = [1,2,3,4,45,-1,-3,-4]
arr.sort()
print(arr)
low = 0
high = len(arr) - 1

target = -4

while low <= high: 
    
    mid = (low + high)//2 #Floor value

    if arr[mid] == target:
        print("The Target element is found!")
        break

    if arr[mid] > target:
        high = high + 1
    elif arr[mid] < target:
        low = low + 1
    