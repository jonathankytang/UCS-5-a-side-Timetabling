#AQA Computer Science Non-Exam Assessment
#Spring 2017
#Candidate Name: Jonathan Tang
#Candidate Number: 9085
#Centre Number: 10283

import itertools
import datetime
import queue as Q
from operator import itemgetter
from itertools import cycle
import csv
import random
from tkinter import *
from tkinter import filedialog
import getpass
import os
import sys
global importSpreadsheet
global window1

class DayofWeekPriority:
    def __init__(self, yeargroup, dayofweek, priority):
        self.yeargroup = yeargroup
        self.dayofweek = dayofweek
        self.priority = priority

    def __cmp__ (self, other):
        return cmp(self.priority, other.priority)

def openSpreadsheet():
    userfileName = VuserfileName.get()
    openfileName = userfileName + ".csv"
    #opens the new fixture list in excel
    if sys.platform == "darwin":
        os.system("open " + openfileName)
        root.destroy()
        window1.destroy()
        sys.exit()
    elif sys.platform == "win32":
        os.system(openfileName)
        root.destroy()
        window1.destroy()
        sys.exit()

def window2Close():
    window2.destroy()

def window3Close():
    window3.destroy()

def quitProgram():
    root.destroy()
    sys.exit()

def assigndatestomatches():
    #retrieves user input for new file name
    userfileName = VuserfileName.get()
    while userfileName != "":
        #retrieves inputted data from user interface
        dayStart = int(VdayStart.get())
        monthStart = int(VmonthStart.get())
        yearStart = int(VyearStart.get())
        dayEnd = int(VdayEnd.get())
        monthEnd = int(VmonthEnd.get())
        yearEnd = int(VyearEnd.get())
        userfileName = VuserfileName.get()

        #GROUP STAGE MATCHES

        #Group stage structure
        lsA = ["E1", "E2", "E3", "E4"]
        lsB = ["S1", "S2", "S3", "S4"]
        msA = ["L1", "L2", "L3", "L4"]
        msB = ["R1", "R2", "R3", "R4"]
        usA = ["U1", "U2", "U3", "U4"]
        usB = ["T1", "T2", "T3", "T4"]
        usC = ["61", "62", "63", "64"]
        usD = ["T5", "61", "T6", "62"]
        mxA = ["M1", "M2", "M3", "M4"]

        #all group stage fixtures
        lsA = list(itertools.combinations(lsA, 2))
        lsB = list(itertools.combinations(lsB, 2))
        msA = list(itertools.combinations(msA, 2))
        msB = list(itertools.combinations(msB, 2))
        usA = list(itertools.combinations(usA, 2))
        usB = list(itertools.combinations(usB, 2))
        usC = list(itertools.combinations(usC, 2))
        usD = list(itertools.combinations(usD, 2))
        mxA = list(itertools.combinations(mxA, 2))

        #re-ordering group fixtures
        lsA = [lsA[0]] + [lsA[5]] + [lsA[1]] + [lsA[4]] + [lsA[2]] + [lsA[3]]
        lsB = [lsB[0]] + [lsB[5]] + [lsB[1]] + [lsB[4]] + [lsB[2]] + [lsB[3]]
        msA = [msA[0]] + [msA[5]] + [msA[1]] + [msA[4]] + [msA[2]] + [msA[3]]
        msB = [msB[0]] + [msB[5]] + [msB[1]] + [msB[4]] + [msB[2]] + [msB[3]]
        usA = [usA[0]] + [usA[5]] + [usA[1]] + [usA[4]] + [usA[2]] + [usA[3]]
        usB = [usB[0]] + [usB[5]] + [usB[1]] + [usB[4]] + [usB[2]] + [usB[3]]
        usC = [usC[0]] + [usC[5]] + [usC[1]] + [usC[4]] + [usC[2]] + [usC[3]]
        usD = [usD[0]] + [usD[5]] + [usD[1]] + [usD[4]] + [usD[2]] + [usD[3]]
        mxA = [mxA[0]] + [mxA[5]] + [mxA[1]] + [mxA[4]] + [mxA[2]] + [mxA[3]]

        matchList = lsA + lsB + msA + msB + usA + usB + usC + usD + mxA

        #converting tuples to lists
        for counter1 in range(len(matchList)):
            list3 = list(matchList[counter1])
            matchList[counter1] = list3

        #assigning match numbers to gs matches
        groupCode = ["LS", "MS", "US", "MX"]
        groupCount = [12, 12, 24, 6]

        match = 0
        for group in range(4):
            for count in range(groupCount[group]):
                matchCode = groupCode[group] + str(count+1)
                matchList[match].append(matchCode)
                match += 1

        #assigning dates
        startDate = datetime.date(yearStart, monthStart, dayStart)
        endDate = datetime.date(yearEnd, monthEnd, dayEnd)

        numberDay = 0
        if startDate.isoweekday() == 1:
            numberDay = 10
        elif startDate.isoweekday() == 2:
            numberDay = 11
        elif startDate.isoweekday() == 3:
            numberDay = 12
        elif startDate.isoweekday() == 4:
            numberDay = 13
        elif startDate.isoweekday() == 5:
            numberDay = 14

        gsEndDate = startDate + datetime.timedelta(days=numberDay)

        koStartDate = gsEndDate + datetime.timedelta(days=(8-gsEndDate.isoweekday()))

        delta = endDate - startDate

        gsdelta = gsEndDate - startDate

        #stores dates into list, adds weekday and match counters for group stages
        datesList = []
        for i in range(gsdelta.days+1):
            newDate = startDate + datetime.timedelta(days=i)
            if newDate.isoweekday()<6:
                datesList += [[newDate.year, newDate.month, newDate.day, newDate.isoweekday(),[0,0,0,0,0,0,0,0],[0,0,0,0]]]

        #priorities for each year group
        priorityGS = []

        priorityVals = {
            "E": [3,5,2],
            "S": [5,4,1,2],
            "L": [3,5,1,2],
            "R": [3,5,4,1],
            "U": [5,4,2],
            "T": [1,4,2],
            "6": [1,4,2],
            "M": [1,4,2]
        }

        for key, value in priorityVals.items():
            for i in range(len(priorityVals[key])):
                priorityGS.append(DayofWeekPriority(key, value[i], i+1))

        #converts Year Groups to Numbers
        yearNum = {
            "E": 0, 
            "S": 1, 
            "L": 2, 
            "R": 3, 
            "U": 4, 
            "T": 5, 
            "6": 6, 
            "M": 7}

        #add dates to GS matches
        for match in matchList:
            priNum = 1
            dateFound = False
            yearGroupcode = match[0][0]
            yearGroup = yearNum[yearGroupcode]
            while dateFound == False:
                dayFound = False
                count = 0
                while dayFound == False:
                    pri = priorityGS[count]
                    if pri.yeargroup == yearGroupcode and pri.priority == priNum:
                        bestDay = pri.dayofweek
                        dayFound = True
                    else:
                        count += 1
                counter = 0
                dateFound = False
                while counter < len(datesList) and dateFound == False:
                    if datesList[counter][3] == bestDay and datesList[counter][4][yearGroup] < 2 and sum(datesList[counter][4]) < 6:
                        match.append(datesList[counter])
                        datesList[counter][4][yearGroup] += 1
                        dateFound = True
                    else:
                        counter += 1
                if dateFound == False:
                    priNum += 1

        #assigns each GS match a pitch
        matchCounter = 0
        for counter in range(len(matchList)):
            if matchCounter % 2 == 0:
                matchList[matchCounter].append("Centre")
                matchCounter += 1
            else:
                matchList[matchCounter].append("Jeremy Bentham")
                matchCounter += 1

        #sorts GS matches into chronological order
        matchList = sorted(matchList, key=itemgetter(3))

        #assigns each GS match a session
        daySessions = [1, 1, 2, 2, 3, 3]
        for match,count in zip(matchList,cycle(daySessions)):
            match.append(count)

        #KNOCKOUT MATCHES

        #Knockout stage structure
        lsKo = [["Winner of Lower School Group A", "Runner up of Lower School Group A", "LS13"],
              ["Winner of Lower School Group B", "Runner up of Lower School Group B", "LS14"],
              ["Winner of Match LS13", "Winner of Match LS14", "LS15"]]
        msKo = [["Winner of Middle School Group A", "Runner up of Middle School Group A", "MS13"],
              ["Winner of Middle School Group B", "Runner up of Middle School Group B", "MS14"],
              ["Winner of Match MS13", "Winner of Match MS14", "MS15"]]
        usKo = [["Winner of Upper School Group A", "Runner up of Upper School Group A", "US25"],
              ["Winner of Upper School Group B", "Runner up of Upper School Group B", "US26"],
              ["Winner of Upper School Group C", "Runner up of Upper School Group C", "US27"],
              ["Winner of Upper School Group D", "Runner up of Upper School Group D", "US28"],
              ["Winner of Match US25", "Winner of Match US26","US29"],
              ["Winner of Match US27", "Winner of Match US28", "US30"],
              ["Winner of Match US29", "Winner of Match US30", "US31"]]
        mxKo = [["Winner of Mixed Group A", "Runner up of Mixed Group A", "MX7"]]

        #priorities for each competition
        priorityKO = []

        priorityKOnums = {
            "LS": [5, 2, 2],
            "MS": [3, 5, 1],
            "US": [4, 2, 2],
            "MX": [4, 2, 2]
        }

        for key, value in priorityKOnums.items():
            for i in range(len(priorityKOnums[key])):
                priorityKO.append(DayofWeekPriority(key, value[i], i+1))

        #data dictionary
        compNum = {"LS": 0, "MS": 1, "US": 2, "MX": 3}

        #adds all the KO fixtures to matchList
        komatchList = []
        finaldayMatches = []

        komatchList += lsKo
        komatchList += msKo
        finaldayMatches.append(usKo.pop())
        komatchList += usKo
        finaldayMatches += mxKo

        #adds on KO dates to KO matches
        numDays = 9

        kodatesList = []
        koEndDate = koStartDate + datetime.timedelta(days=numDays)
        kodelta = koEndDate - koStartDate

        for i in range (kodelta.days + 1):
            newDate = koStartDate + datetime.timedelta(days = i)
            if newDate.isoweekday()<6:
                kodatesList += [[newDate.year, newDate.month, newDate.day, newDate.isoweekday(),[0,0,0,0,0,0,0,0],[0,0,0,0]]]

        for match in komatchList:
            priNum = 1
            dateFound = False
            competition = compNum[match[2][:2]]
            while dateFound == False:
                dayFound = False
                count = 0
                while dayFound == False:
                    pri = priorityKO[count]
                    if pri.yeargroup == match[2][:2] and pri.priority == priNum:
                        bestDay = pri.dayofweek
                        dayFound = True
                    else:
                        count += 1
                counter = 0
                dateFound = False
                if match[0][10:15] == "match":
                    pre1 = match[0][16:20]
                    matchCounter = 0
                    preFound = False
                    while preFound == False:
                        if komatchList[matchCounter][2] == pre1:
                            date1 = komatchList[matchCounter][3][:3]
                            preFound = True
                        else:
                            matchCounter += 1
                    pre2 = match[1][16:20]
                    matchCounter = 0
                    preFound = False
                    while preFound == False:
                        if komatchList[matchCounter][2] == pre2:
                            date2 = komatchList[matchCounter][3][:3]
                            preFound = True
                        else:
                            matchCounter += 1
                    datesFound = 0
                    while datesFound < 2:
                        if kodatesList[counter][:3] == date1:
                            datesFound += 1
                        if kodatesList[counter][:3] == date2:
                            datesFound += 1
                        counter += 1
                while counter < len(kodatesList) and dateFound == False:
                    if (kodatesList[counter][3] == bestDay or match[2] == "US29" or match[2] == "US30") and kodatesList[counter][5][competition] < 2 and sum(kodatesList[counter][5]) < 6:
                        match.append(kodatesList[counter])
                        kodatesList[counter][5][competition] += 1
                        dateFound = True
                    else:
                        counter += 1
                if dateFound == False:
                    if priNum < 3:
                        priNum += 1
                    else:
                        enoughDates = False
                        y += 1
                        break

        finalDate = koEndDate + datetime.timedelta(days=1)
        finalDateConv = [finalDate.year, finalDate.month, finalDate.day, finalDate.isoweekday(), [0,0,0,0,0,0,0,0],[0,0,1,1]]

        for match in finaldayMatches:
            match.append(finalDateConv)

        #sorts KO matches into chronological order
        komatchList += finaldayMatches
        komatchList = sorted(komatchList, key=itemgetter(3))

        #assigning pitches and session times to KO matches
        prevDate = []
        for match in komatchList:
            if match[3] != prevDate:
                pitch = 1
            else:
                pitch += 1

            match.append("Centre")
            match.append(pitch)
            prevDate = match[3]

        matchList += komatchList
        kodatesList += [finalDateConv]
        datesList += kodatesList

        #import csv files
        user = getpass.getuser()
        importSpreadsheet = filedialog.askopenfilename(initialdir="C:/Users/%s" % user)

        #retreives data from spreadsheet and assigns team names to team codes
        while importSpreadsheet[-4:] == ".csv":
            with open(importSpreadsheet) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=",")

                importedE = []
                importedS = []
                importedL = []
                importedR = []
                importedU = []
                importedT = []
                imported6 = []
                importedM = []

                for row in readCSV:
                    if row[3] == "Lower School (Entry, Shell)":
                        if row[4] == "Entry":
                            importedE.append(row[5])

                        if row[4] == "Shell":
                            importedS.append(row[5])

                    if row[3] == "Middle School (Lower Remove, Remove)":
                        if row[4] == "Lower Remove":
                            importedL.append(row[5])

                        if row[4] == "Remove":
                            importedR.append(row[5])

                    if row[3] == "Upper School (Upper Remove, Transitus, Sixth, BOYS only)":
                        if row[4] == "Upper Remove":
                            importedU.append(row[5])

                        if row[4] == "Transitus":
                            importedT.append(row[5])

                        if row[4] == "Sixth":
                            imported6.append(row[5])

                    if row[3] == "Mixed (Transitus, Sixth, Boys AND Girls)":
                        importedM.append(row[5])

                #randomises teams in each group
                random.shuffle(importedE)
                random.shuffle(importedS)
                random.shuffle(importedL)
                random.shuffle(importedR)
                random.shuffle(importedU)
                random.shuffle(importedT)
                random.shuffle(imported6)
                random.shuffle(importedM)

            #re-order matches
            finalmatchList = []
            counter = 0
            for counter in range(len(matchList)):
                year = matchList[counter][3][0]
                month = matchList[counter][3][1]
                day = matchList[counter][3][2]
                date = str(year) +"/"+str(month)+"/"+str(day)
                date_object = datetime.datetime.strptime(date, "%Y/%m/%d")
                convertedDate = date_object.strftime("%a-%d-%b")
                weekday = matchList[counter][3][3]
                matchNo = matchList[counter][2]
                team1 = matchList[counter][0]
                team2 = matchList[counter][1]

                #assigning pitches and sessions to komatches
                if len(team1) == 2:

                    yr = team1[0]
                    nm = int(team1[1])

                    if yr == "E":
                        team1 = importedE[nm-1]
                    elif yr == "S":
                        team1 = importedS[nm-1]
                    elif yr == "L":
                        team1 = importedL[nm-1]
                    elif yr == "R":
                        team1 = importedR[nm-1]
                    elif yr == "U":
                        team1 = importedU[nm-1]
                    elif yr == "T":
                        team1 = importedT[nm-1]
                    elif yr == "6":
                        team1 = imported6[nm-1]
                    elif yr == "M":
                        team1 = importedM[nm-1]

                    yr = team2[0]
                    nm = int(team2[1])

                    if yr == "E":
                        team2 = importedE[nm-1]
                    elif yr == "S":
                        team2 = importedS[nm-1]
                    elif yr == "L":
                        team2 = importedL[nm-1]
                    elif yr == "R":
                        team2 = importedR[nm-1]
                    elif yr == "U":
                        team2 = importedU[nm-1]
                    elif yr == "T":
                        team2 = importedT[nm-1]
                    elif yr == "6":
                        team2 = imported6[nm-1]
                    elif yr == "M":
                        team2 = importedM[nm-1]

                session = matchList[counter][5]
                pitch = matchList[counter][4]
                finalmatchList.append([convertedDate,  matchNo, team1,"", team2,"", session, pitch])
                counter += 1

            #sorts finalmatchList in chronological order
            finalmatchList = sorted(finalmatchList, key = lambda row: datetime.datetime.strptime(row[0], "%a-%d-%b"))

            #delete matchlist, & add column headings
            del matchList
            finalmatchList.reverse()
            finalmatchList.append(["Date", "Match No", "Home Team", "", "Away Team", "", "Session", "Pitch"])
            finalmatchList.reverse()

            #write csv
            newFile = open(userfileName + ".csv", "w")
            writenewFile = csv.writer(newFile)
            writenewFile.writerows(finalmatchList)
            newFile.close()

            #User Interface - Prompt Window to open new file
            global window1
            window1 = Tk()
            window1.title = ("Open Spreadsheet")
            window1Header1 = Label(window1,text="The fixtures list has been built", font="Arial 18")
            window1Header1.pack()
            window1Header2 = Label(window1, text="Click open below to open the new spreadsheet", font="Arial 18")
            window1Header2.pack()
            window1Header3 = Label(window1, text="Once open is clicked this program will close", font="Arial 10")
            window1Header3.pack()
            button3 = Button(window1, text="Open", command=openSpreadsheet)
            button3.pack()
            window1.mainloop()

        else:
            #User Interface - error message for selecting a file that is not .csv format
            global window2
            window2 = Tk()
            window2.title = ("Error")
            window2Header1 = Label(window2, text="ERROR", font="Arial 36 bold")
            window2Header1.pack()
            window2Header2 = Label(window2, text="Please select a file ending in .csv", font="Arial 18")
            window2Header2.pack()
            button4 = Button(window2, text="Close", command=window2Close)
            button4.pack()
            window2.mainloop()

    else:
        #User Interface - error message for not inputting a new file name
        global window3
        window3 = Tk()
        window3.title = ("Error")
        window3Header1 = Label(window3, text="ERROR", font="Arial 36 bold")
        window3Header1.pack()
        window3Header2 = Label(window3, text="Please enter a new file name ", font="Arial 18")
        window3Header2.pack()
        button5 = Button(window3, text="Close", command=window3Close)
        button5.pack()
        window3.mainloop()

if __name__ == '__main__':

    #User Interface - Home Screen
    root=Tk()
    root.title = ("Start & End Dates")
    root.geometry =("500 x 500")

    VdayStart = IntVar()
    VmonthStart = IntVar()
    VyearStart = IntVar()
    VdayEnd = IntVar()
    VmonthEnd = IntVar()
    VyearEnd = IntVar()
    VuserfileName = StringVar()

    VdayStart.set(9)
    VmonthStart.set(1)
    VyearStart.set(2017)
    VdayEnd.set(9)
    VmonthEnd.set(2)
    VyearEnd.set(2017)
    VuserfileName.set("test.csv")

    button1 = Button(root, text="Quit Program", command=quitProgram).grid(row=1, column=3)

    logo = PhotoImage(file="UCS_Roundel_RGB.gif")
    img = Label(root, image = logo).grid(row=2, column=1, columnspan=3)

    header1 = Label(root, text="University College School Community Action", fg="#660033", font="Arial 30 bold").grid(row=3, column=1, columnspan=3)
    header2 = Label(root, text="5-A-Side Football Competition Fixture List Builder", font="Arial 20 bold").grid(row=4, column=1, columnspan=3)
    blank1 = Label(root, text="").grid(row=5, column=1, columnspan=3)

    introMessage1 = Label(root,text="Welcome!", font="Arial 26").grid(row=6, column=1, columnspan=3)
    introMessage2 = Label(root,text="To create a fixture list, follow the instructions below").grid(row=7, column=1, columnspan=3)
    blank2 = Label(root,text="").grid(row=8, column=1, columnspan=3)

    dateHeader = Label(root, text="Start & End Dates", font="Arial 18 bold").grid(row=9, column=1, columnspan=3)
    partMessage = Label(root,text="Please enter fill in all the fields below").grid(row=10, column=1, columnspan=3)

    startLabel = Label(root,text="START DATE").grid(row=11, column=1, columnspan=3)
    daystartLabel = Label(root, text= "Enter start day: ").grid(row=12, column=1)
    monthstartLabel = Label(root, text= "Enter start month:").grid(row=12, column=2)
    yearstartLabel = Label(root, text="Enter start year:").grid(row=12, column=3)
    daystartTb = OptionMenu(root,VdayStart,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                        16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31).grid(row=13, column=1)
    monthstartTb = OptionMenu(root, VmonthStart,1,2,3,4,5,6,7,8,9,10,11,12).grid(row=13, column=2)
    yearstartTb = OptionMenu(root, VyearStart,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,
                         2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,
                         2041,2042,2043,2044,2045,2046,2047,2048,2049,2050).grid(row=13, column=3)

    endLabel = Label(root,text="END DATE").grid(row=14, column=1, columnspan=3)
    dayendLabel = Label(root, text= "Enter end day: ").grid(row=15, column=1)
    monthendLabel = Label(root, text= "Enter end month:").grid(row=15, column=2)
    yearendLabel = Label(root, text="Enter end year:").grid(row=15, column=3)
    dayendTb = OptionMenu(root, VdayEnd,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                        16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31).grid(row=16, column=1)
    monthendTb = OptionMenu(root, VmonthEnd,1,2,3,4,5,6,7,8,9,10,11,12).grid(row=16, column=2)
    yearendTb = OptionMenu(root, VyearEnd,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,
                         2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,
                         2041,2042,2043,2044,2045,2046,2047,2048,2049,2050).grid(row=16, column=3)
    blank3 = Label(root,text="").grid(row=17, column=1)

    userfilenameHeader = Label(root, text="New File Name", font="Arial 18 bold").grid(row=18, column=1, columnspan=3)
    userfilenameLabel = Label(root, text="Enter the file name of your fixture list").grid(row=19, column=1, columnspan=2)
    userfilenameTb = Entry(root, textvariable=VuserfileName, justify="left").grid(row=19, column=3)
    blank4 = Label(root, text="").grid(row=20, column=1)

    button2Header = Label(root,text="Click next to import spreadsheet", font="Arial 18 bold").grid(row=21, column=1, columnspan=3)
    button2 = Button(root, text ="Next", command=assigndatestomatches).grid(row=22, column=1, columnspan=3)

    root.mainloop()