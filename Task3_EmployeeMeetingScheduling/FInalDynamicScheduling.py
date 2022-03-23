import time
import csv
import Conversions
import differentListsConversionLoops

'''
csvData = open('employeeDailyData.csv', 'a', newline="")
csvWriteData = csv.writer(csvData, delimiter=",")
csvWriteData.writerows([

    ["10:00", "18:00", "13:00", "14:00"],
    ["11:00", "19:00", "13:00", "14:00"],
    ["12:00", "18:00", "14:00", "15:00"],
    ["11:00", "17:00", "13:00", "14:00"],
    ["12:00", "20:00", "15:00", "16:00"]

])

'''
# Part 2 | CSV Data Reading
# employeeTableString = [
#     ["10:00", "18:00", "13:00", "14:00"],
#     ["11:00", "19:00", "13:00", "13:30"],
#     ["12:00", "18:00", "14:00", "14:30"],
#     ["11:00", "17:00", "13:00", "14:00"]
# ]

# Converts the String standard time to Minutes, Including the Breaks

csvWrite = open("MeetingsTimeline.csv", 'w', newline='')
csvWriteData = csv.writer(csvWrite, delimiter=",")
csvWriteData.writerow(["People Involved", "Starting Time", "Ending Time"])

while True:

    print(" ____________________________________________")
    print("|                                            |")
    print("|                   WELCOME                  |")
    print("|                      To                    |")
    print("|         EMPLOYEE MANAGEMENT SYSTEM         |")
    print("|____________________________________________|")

    print("The employees we have:")
    print("0: Shyam")
    print("1: Aditya")
    print("2: Naga")
    print("3: Prashanth")

    print("Who all you'd want to schedule meeting with me?")
    employeeInputList = []
    employeeInputList.append(int(input("Enter the first Employee ID")))
    startCounter = 0
    while True:
        if startCounter == 0:
            employeeInputList.append(int(input("Enter the next employee ID")))
        else:
            x = int(input(
                "Enter the next employee, If you don't have any in mind enter the NUMBER 10"))
            if x != 10:
                employeeInputList.append(x)
            else:
                break
        startCounter += 1

    print("Great!, This is the IDs data you've inputted {}".format(employeeInputList))
    meetingDuration = (input(print("Now input the MEETING DURATION: ")))

    meetingDurationConverted = Conversions.hrToMinInteger(meetingDuration)
    print(meetingDurationConverted)

    # Find Maximum of the In Times | Kadane's Algorithm
    maxTime = 0
    maxTimeArray = []

    for x in employeeInputList:
        for y in range(len(differentListsConversionLoops.meetingsTimeline[x])-1):

            if y == 0:
                diff = abs(differentListsConversionLoops.meetingsTimeline[x][y]
                           [0] - differentListsConversionLoops.meetingsTimeline[x][y+1][0])
                if meetingDurationConverted <= diff:
                    maxTimeArray.append(differentListsConversionLoops.meetingsTimeline[x][y][0])
                    break
            else:
                diff = abs(differentListsConversionLoops.meetingsTimeline[x][y]
                           [1] - differentListsConversionLoops.meetingsTimeline[x][y+1][0])
                if meetingDurationConverted <= diff:
                    maxTimeArray.append(differentListsConversionLoops.meetingsTimeline[x][y][1])
                    break

            y += 1

        maxTime = max(maxTimeArray)
        print(maxTime)
        print(maxTimeArray)

    outMax = []
    for x in differentListsConversionLoops.inOutList:
        outMax.append(x[1])
    largestRange = max(outMax)

    while True:
        #possi = []
        maxTimeCounter = 0
        for x in employeeInputList:
            print(x)
            for y in range(len(differentListsConversionLoops.meetingsTimeline[x])-1):
                if y == 0:
                    if differentListsConversionLoops.meetingsTimeline[x][y][0] <= maxTime and differentListsConversionLoops.meetingsTimeline[x][y+1][0] >= maxTime + meetingDurationConverted:
                        maxTimeCounter += 1
                    # Can take an array of possible places to insert, If the break is removed
                        # possi.append(meetingsTimeline[x][y][0])
                else:
                    if differentListsConversionLoops.meetingsTimeline[x][y][1] <= maxTime and differentListsConversionLoops.meetingsTimeline[x][y+1][0] >= maxTime + meetingDurationConverted:
                        maxTimeCounter += 1
                        # possi.append(meetingsTimeline[x][y][1])

        # print(possi)

        c = 0
        if maxTimeCounter == len(employeeInputList):
            for x in employeeInputList:
                temp = []
                for y in range(1):
                    temp.append(maxTime)
                    temp.append(maxTime+meetingDurationConverted)

                differentListsConversionLoops.meetingsTimeline[x].append(temp)
                differentListsConversionLoops.meetingsTimeline[x].sort()
                
                updation_meet_timeStart = maxTime
                updation_meet_timeEnd  = maxTime+meetingDurationConverted
                
                if c == 0:
                    print("Meeting is booked at {} and goes on uptill {}".format(
                        Conversions.minutesToHours(temp[0]), Conversions.minutesToHours(temp[1])))
                c += 1
            break
        else:
            maxTime += meetingDurationConverted

        if maxTime >= largestRange:
            print("Scheduling Not Possible, Pick other duration!!")
            break

    for x in employeeInputList:
        print(differentListsConversionLoops.meetingsTimeline[x])
    
    #updation_time_employee = time.ctime()
    updation_employees_involved = employeeInputList
    
    csvWriteData.writerow(
      [updation_employees_involved, updation_meet_timeStart//60, updation_meet_timeEnd//60]  
    )

    choice = input("You'd want to schedule another meeting? [Y/N]")
    if choice == "Y":
        pass
    else:
        break

    # Second Half post the break
