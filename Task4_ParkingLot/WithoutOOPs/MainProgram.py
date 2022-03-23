
import time
from dictions import dictionArea, dictionVehicles

# Depth = Volume/ Area

# 1. TODO: Lot Allocation 

serials = ['A', 'B', 'C', 'D']

while True:
    print("Welcome to Parking LoT!")
    print("1. Parking")
    print("2. Check-out/ De-Allocate")
    print("3. Status of Parkings")
    print("4. Exit")
    choice = int(input("Enter what you'd want to do?"))

    if choice == 1:
        vehicle = input("Car/ Bike/ Bus? Choose one")
        carNumber = input("Enter the Car Number")
        width = int(input("Enter the width of the {}".format(vehicle)))
        depth = int(input("Enter the depth of the {}".format(vehicle)))
        length = int(input("Enter the Length of the {}".format(vehicle)))
        area = length * width
        inTime = time.ctime()

        inTimeSplit = inTime.split(" ")
        print(inTimeSplit[3])
        inTimeSplitDate = inTimeSplit[3].split(":")

        inTimeSplitDateSeconds = int(inTimeSplitDate[2]) * 60

        vehicularCurrent = dictionArea['A'][vehicle] - area
        noPlace = False

        if vehicle == 'car':
            if vehicularCurrent - area < 0:
                print("There's no Space in this series")
                noPlace = True
            else:
                print("Parked!")
                dictionArea['A'][vehicle] -= area
                dictionVehicles['A'][vehicle][carNumber] = {'length':length, 'width': width, 'inTime': inTimeSplitDateSeconds}
        elif vehicle == 'bike':
            if vehicularCurrent - area < 0:
                print("There's no Space in this series")
                noPlace = True
            else:
                print("Parked!")
                dictionArea['A'][vehicle] -= area
                dictionVehicles['A'][vehicle][carNumber] = {'length':length, 'width': width, 'inTime': inTimeSplitDateSeconds}
        elif vehicle == 'bus':
            if vehicularCurrent - area < 0:
                print("There's no Space in this series")
                noPlace = True
            else:
                print("Parked!")
                dictionArea['A'][vehicle] -= area
                dictionVehicles['A'][vehicle][carNumber] = {'length':length, 'width': width, 'inTime': inTimeSplitDateSeconds}

        if noPlace == True:

            counter = 0

            for x in serials:

                if dictionArea[x][vehicle] - area < 0:
                    counter += 1

                    if counter == 4:
                        print("There's no space for your vehicle in our Parking Lot")
                        print("Sorry for the inconvienence.")
                        print("")
                    continue
                else:
                    dictionArea[x][vehicle] -= area
                    dictionVehicles[x][vehicle][carNumber] = {'length':length, 'width': width, 'inTime': inTimeSplitDateSeconds}
                    print("Parked at {}!".format(x))
                    break
            noPlace = False

    elif choice == 2:
        checkoutSerial = input("Enter the Serial Number given")
        checkoutVehicle = input("Enter your vehicle type")
        checkoutCarNumber = input("Enter your Car Number")

        outTime = time.ctime()
        outTimeSplit = outTime.split(" ")
        print(outTimeSplit[3])
        outTimeSplitDate = outTimeSplit[3].split(":")
        outTimeSplitDateSeconds = int(outTimeSplitDate[2]) * 60

        duration = abs(dictionVehicles[checkoutSerial][checkoutVehicle][checkoutCarNumber]['inTime'] - outTimeSplitDateSeconds)
        tempLen = dictionVehicles[checkoutSerial][checkoutVehicle][checkoutCarNumber]['length']
        tempWidth = dictionVehicles[checkoutSerial][checkoutVehicle][checkoutCarNumber]['width']
        tempArea = tempLen * tempWidth
        dictionArea[checkoutSerial][checkoutVehicle] += tempArea
        dictionVehicles[checkoutSerial][checkoutVehicle].pop(checkoutCarNumber)

        if duration >= 30 and duration<60:
            amountPayable = 20
        elif duration >= 60 and duration <= 600: 
            amountPayable = duration // 60 * 10
        elif duration >= 600:
            amountPayable = duration // 60 * 5
        print("Thanks for visiting us!")
        print("Amount payable: {}".format(amountPayable))
        print("")

    elif choice == 3:
        for keys, values in dictionVehicles.items():
            print("Serial {}".format(keys))
            for zKeys, zValues in values.items():
                print("The Vehicle Type {}".format(zKeys))
                for yKeys, yValues in zValues.items():
                    print("The Car Number {}".format(yKeys))
                    print("InTime: {}".format(yValues['inTime']))
                
                print("-------------------------")
                print("")
    elif choice == 4:
        break


# TODO: CSV Writing