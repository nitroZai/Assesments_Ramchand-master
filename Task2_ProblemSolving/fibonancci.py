
fib1 = 0 
fib2 = 1
fibSum = 0
upto = 10

print(fib1, fib2)
for x in range(2, upto):

    temp = fib1
    fib1 = fib2
    fib2 = temp + fib1

    print(fib2)
