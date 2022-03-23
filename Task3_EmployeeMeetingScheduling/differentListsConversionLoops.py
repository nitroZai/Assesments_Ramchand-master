import csv
import Conversions

csvData = open('employeeDailyData.csv', encoding="UTF-8")
csvReaderData = csv.reader(csvData)

employeeTableString = []
for i in csvReaderData:
    employeeTableString.append(i)

employeeTableMinutes = []

for x in employeeTableString:

    temp = []
    for y in x:

        temp.append(Conversions.hrToMinString(y))

    employeeTableMinutes.append(temp)

# print(employeeTableMinutes)

# Breaking the Array minutes into two another Arrays

breakList = []
inOutList = []

# Filling the two above Arrays with our 2D array data.

for x in range(len(employeeTableMinutes)):

    temp = []
    for y in range(2):
        temp.append(employeeTableMinutes[x][y])

    inOutList.append(temp)


for x in range(len(employeeTableMinutes)):

    temp = []
    for y in range(2, len(employeeTableMinutes[0])):
        temp.append(employeeTableMinutes[x][y])

    breakList.append(temp)

# Building the Meetings Timelines List

meetingsTimeline = []

for x in range(len(inOutList)):
    temp = []
    for y in range(1):
        temp1 = []
        temp2 = []
        temp1.append(inOutList[x][y])
        temp2.append(inOutList[x][y+1])
    temp.append(temp1)
    temp.append(breakList[x])
    temp.append(temp2)
    meetingsTimeline.append(temp)
print("The meeting timeline Intial:")
print(meetingsTimeline)
