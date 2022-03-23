# Power of two
n = 64

if n > 0 and n & (n - 1) == 0:
    print(f"{n} is a power of two")
else:
    print(f"{n} isn't a power of 2")


# Power of Three
n = 81

while n % 3 == 0:
    n = n/3

if n == 1:
    print("{} is a power of Three".format(n))
else:
    print("{} isn't a power of Three".format(n))


# Power of Four

n = 64

if n % 10 == 4 or n % 10 == 6:
    if n & n - 1 == 0:
        print("{} is a power of four".format(n))
    else:
        print("{} isnt a power of four".format(n))