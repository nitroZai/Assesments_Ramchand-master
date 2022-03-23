from csv import reader

import csv

(print("Hello User!"))
tempList = []

while True:

    choice = int(input("1. Add Rows\n 2. Check The Added Data\n 3. Exit\n"))

    if choice == 1:
        
        data = open('spreadsheet1.csv', 'w', newline= '', encoding='utf-8')
        csv_write = csv.writer(data, delimiter=',')
        
        for x in range( 0, 3 ):
            tempList.append(input("Name | College | Grade"))

        csv_writerows = csv_write.writerows(tempList)
    elif choice == 2:

        readData = open('spreadsheet1.csv', encoding='utf-8')
        csv_data = list(csv.reader(readData))

        print(csv_data)
    elif choice == 3:

        break



    # elif choice == 2:

    # elif choice == 3:
    #     break
        


    # for x in range(0, 3):
    #     tempList[x].append(input("Enter Name+College+Grade"))



    

    # finally:

    # data = open('spreadsheet1.csv', 'w', newline= '', encoding='utf-8')
    # csv_writer = csv.writer(data, delimiter=',')
    # csv_rows = csv_writer.writerow(['Name','College','Grade'])

    # data = open('spreadsheet1.csv', encoding='utf-8')
    # csv_data = list(csv.reader(data))
    # print(csv_data)


