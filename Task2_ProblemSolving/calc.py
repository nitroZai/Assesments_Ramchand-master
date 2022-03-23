
#TODO: Input has to handled 

n1 = int(input("Enter the number"))
count = 0

choice = ""
while choice!= "no":
    # Only in the first iteration we will have to take inputs twice for 
    # the rest of the operations we will be skipping the first input
    if count != 0:
        n1 = result

    n2 = int(input("Enter the other number"))
    op = input("Enter the operation")

    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2
    elif op == "%":
        result = n1%n2

    count += 1
    print("Would you want to continue again? If not press no")
    choice = input("")
    if choice == "no": break

        
print("The output: {}".format(result))