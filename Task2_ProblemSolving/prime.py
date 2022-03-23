
# Program to check whether a certain range is prime or not
# Time Complexity O(nLog(n))

startRange = int(input("Enter the first Range number"))
endRange = int(input("Enter the Second Range number"))

counter = 0 

for x in range(startRange, endRange+1):

    if startRange == 2:
        print("2 is a prime")
        continue

    for y in range(2, x//2+1):
        if x % y == 0:
            counter += 1
            print(f"{x} Isn't a Prime Number")
            break
    
    if counter == 0:
        print(f"{x} is a prime") 

    counter = 0