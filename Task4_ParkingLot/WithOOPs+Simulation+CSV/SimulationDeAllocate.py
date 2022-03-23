import csv
import time
import random

class Vehicle(object):

    def __init__(self, length, width, vType) -> None:
        self.length = length
        self.width = width
        self.vType = vType

    def getArea(self):
        return (self.length * self.width)

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width
    def getvType(self):
        return self.vType

class Bike(Vehicle):
    def __init__(self, length, width, vType) -> None:
        super().__init__(length, width, vType)

class Car(Vehicle):
    def __init__(self, length, width, vType) -> None:
        super().__init__(length, width, vType)

class Bus(Vehicle):
    def __init__(self, length, width, vType) -> None:
        super().__init__(length, width, vType)

class ParkingLot(object):

    lotLength = 100
    lotWidth = 10
    lotArea = lotLength * lotWidth

    dictionArea = {
        'A':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        },
        'B':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        },
        'C':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        },
        'D':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        }
    }

    def __init__(self, length, width) -> None:
        self.lotLength = length
        self.lotWidth = width        

    def setLotArea(self):
        self.lotArea = self.lotLength * self.lotWidth
    
    def getLotArea(self):
        self.lotArea = self.lotLength * self.lotWidth
        return self.lotArea

if __name__ == '__main__':
    parkingLot = ParkingLot(100,10)
    parkingLot.setLotArea()
    
    # Allocation CSV File
    csvData = open('Allocation.csv', 'a', newline='')
    csvDataWriter = csv.writer(csvData)

    csvSecondData = open('parkingLotData.csv','w', newline='')
    csvWrite = csv.writer(csvSecondData, delimiter=',')
    csvWrite.writerow(['Serial', 'Vehicle Number', 'In Time', 'Out Time', 'Checkout Amount'])

    serials = ['A', 'B', 'C', 'D'] 
    choiceVehicle = ''

    tempCarArea = 20
    tempBikeArea = 10
    tempBusArea = 50
    
    bikeCounter = 0
    carCounter = 0
    busCounter = 0

    while True:

        print("Welcome De-Allocation Simulation")
        print("bike")
        print("car")
        print("bus")
        print("4. Exit()")
        deAllocateChoice = input("Enter your Choice: ")

        if bikeCounter >119 and deAllocateChoice == 'bike':
            print("All the bikes have been removed already!")
            break
        elif carCounter >119 and deAllocateChoice == 'car':
            print("All the Cars have been removed already!")
            break
        elif busCounter >7 and deAllocateChoice == 'bus':
            print("All Buses have been removed already")
            break

        if deAllocateChoice == 'bike':
            while True:
                flag = 0
                bikeCounter += 1
                vehicleNumber = bikeCounter
                vehicleType = deAllocateChoice
                
                if bikeCounter >= 120:
                    break

                with open('Allocation.csv',newline='') as f:
                    r = csv.reader(f)
                    data = []

                    for x in r:
                        if x[2] == vehicleNumber and x[1] == vehicleType:
                            parkingLot.dictionArea[x[0]][vehicleType] += ar
                            flag = 1
                            tempInTime = int(x[3])
                            outTime = random.randint(0,24)
                            if tempInTime == outTime:
                                outTime = random.randint(0,24)

                            counter = 0
                            tempOutTime = outTime
                            tempTempInTime = tempInTime
                            
                            if tempOutTime < tempTempInTime:
                                    
                                    while True:
                                        if tempOutTime == 24:
                                            break
                                        tempOutTime += 1
                                        counter += 1
                                    
                                    duration = (counter + outTime) * 60
                            else:
                                duration = abs(outTime - tempInTime) * 60

                            print("InTime", tempInTime)
                            print("OutTime", outTime)

                            amountPayable = 0

                            #print(parkingLot.dictionVehicleAllocation)

                            if duration >= 30 and duration <= 60:
                                amountPayable += 20
                            elif duration >= 60 and duration <= 600:
                                amountPayable = (duration // 60) * 10
                            elif duration > 600:
                                amountPayable = (duration // 60) * 5
                            csvSecondData = open('parkingLotData.csv','a', newline='')
                            csvWrite.writerow([x[0] ,vehicleNumber, tempInTime, outTime, amountPayable])
                            
                            if flag == 0:
                                print("The entered Car Number isn't Valid")
                            else:
                                print("Thanks for Visiting us!")
                                print("Amount payable: {}".format(amountPayable))
                            continue

                        data.append(x)

                with open('Allocation.csv','w',newline='') as f:
                    w = csv.writer(f)
                    #w.writerow(['Serial', 'Vehicle Type', 'Vehicle Number', 'inTime'])
                    w.writerows(data)
        elif deAllocateChoice == 'car':
            while True:
                flag = 0
                carCounter += 1
                vehicleNumber = carCounter
                vehicleType = deAllocateChoice
                
                if carCounter >= 120:
                    break

                with open('Allocation.csv',newline='') as f:
                    r = csv.reader(f)
                    data = []

                    for x in r:
                        if x[2] == vehicleNumber:
                            if vehicleType == 'bike':
                                ar = tempBikeArea
                            elif vehicleType == 'car':
                                ar = tempCarArea
                            elif vehicleType == 'bus':
                                ar = tempBusArea
                            parkingLot.dictionArea[x[0]][vehicleType] += ar
                            flag = 1
                            tempInTime = int(x[3])
                            outTime = random.randint(0,24)
                            if tempInTime == outTime:
                                outTime = random.randint(0,24)

                            counter = 0
                            tempOutTime = outTime
                            tempTempInTime = tempInTime
                            
                            if tempOutTime < tempTempInTime:
                                    
                                    while True:
                                        if tempOutTime == 24:
                                            break
                                        tempOutTime += 1
                                        counter += 1
                                    
                                    duration = (counter + outTime) * 60
                            else:
                                duration = abs(outTime - tempInTime) * 60

                            print("InTime", tempInTime)
                            print("OutTime", outTime)

                            amountPayable = 0

                            #print(parkingLot.dictionVehicleAllocation)

                            if duration >= 30 and duration <= 60:
                                amountPayable += 20
                            elif duration >= 60 and duration <= 600:
                                amountPayable = (duration // 60) * 10
                            elif duration > 600:
                                amountPayable = (duration // 60) * 5
                            csvSecondData = open('parkingLotData.csv','a', newline='')
                            csvWrite.writerow([x[0] ,vehicleNumber, tempInTime, outTime, amountPayable])
                            
                            if flag == 0:
                                print("The entered Car Number isn't Valid")
                            else:
                                print("Thanks for Visiting us!")
                                print("Amount payable: {}".format(amountPayable))
                            continue

                        data.append(x)

                with open('Allocation.csv','w',newline='') as f:
                    w = csv.writer(f)
                    #w.writerow(['Serial', 'Vehicle Type', 'Vehicle Number', 'inTime'])
                    w.writerows(data)
        elif deAllocateChoice == 'bus':
            while True:
                flag = 0
                busCounter += 1
                vehicleNumber = busCounter
                vehicleType = deAllocateChoice
                
                if busCounter >= 120:
                    break

                with open('Allocation.csv',newline='') as f:
                    r = csv.reader(f)
                    data = []

                    for x in r:
                        if x[2] == vehicleNumber:
                            if vehicleType == 'bike':
                                ar = tempBikeArea
                            elif vehicleType == 'car':
                                ar = tempCarArea
                            elif vehicleType == 'bus':
                                ar = tempBusArea
                            parkingLot.dictionArea[x[0]][vehicleType] += ar
                            flag = 1
                            tempInTime = int(x[3])
                            outTime = random.randint(0,24)
                            if tempInTime == outTime:
                                outTime = random.randint(0,24)

                            counter = 0
                            tempOutTime = outTime
                            tempTempInTime = tempInTime
                            
                            if tempOutTime < tempTempInTime:
                                    
                                    while True:
                                        if tempOutTime == 24:
                                            break
                                        tempOutTime += 1
                                        counter += 1
                                    
                                    duration = (counter + outTime) * 60
                            else:
                                duration = abs(outTime - tempInTime) * 60

                            print("InTime", tempInTime)
                            print("OutTime", outTime)

                            amountPayable = 0

                            #print(parkingLot.dictionVehicleAllocation)

                            if duration >= 30 and duration <= 60:
                                amountPayable += 20
                            elif duration >= 60 and duration <= 600:
                                amountPayable = (duration // 60) * 10
                            elif duration > 600:
                                amountPayable = (duration // 60) * 5
                            csvSecondData = open('parkingLotData.csv','a', newline='')
                            csvWrite.writerow([x[0] ,vehicleNumber, tempInTime, outTime, amountPayable])
                            
                            if flag == 0:
                                print("The entered Car Number isn't Valid")
                            else:
                                print("Thanks for Visiting us!")
                                print("Amount payable: {}".format(amountPayable))
                            continue

                        data.append(x)

                with open('Allocation.csv','w',newline='') as f:
                    w = csv.writer(f)
                    #w.writerow(['Serial', 'Vehicle Type', 'Vehicle Number', 'inTime'])
                    w.writerows(data)
        else:
            break
    