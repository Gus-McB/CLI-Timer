import csv, Clock, task


class CSVAccess:
    def __init__(self, fileName):
        self.fileName = fileName

    def Time(self, timeSplit): #Makes the time data from the csv file useable for the timer.
        hoursINt, minutesInt, secondsINT = timeSplit.split(":")
        hours = hoursINt
        minutes = minutesInt
        seconds = secondsINT
        return hours, minutes, seconds

    def timeImport(self, fileName): #Imports the data from the csv file.
            with open(fileName + ".csv") as data:
                timeData = csv.reader(data, delimiter=',')
                csvList = []
                for row in timeData:
                    csvList.append(row)
            return csvList

    def writeTask(self): #Allows the user to write their own timer task to be added into the csv file.
        with open(self.fileName + ".csv", 'a', newline='') as file:
            writer = csv.writer(file)
            name = input("Name of timer: ") 
            time = input("Enter time: HH:MM:SS: ")
            writer.writerow([name, time])
            another = input("Would you like to write another task: y/n")
            if another == "n":
                run = False
            else:
                print("New Task")
    
    def exportTasks(self, nameList, agendaList): #Create a csv file and write the tasks that are stored inside.
        with open(self.fileName + '.csv', 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            index = 0
            while index < len(nameList):
                writer.writerow([nameList[index], agendaList[index]])
                index += 1

    def importTask(self): #Takes the data from the csv and displays it to the terminal.
        try:
            with open(self.fileName + ".csv") as file:
                display = csv.reader(file)
                for row in display:
                    print(row)
        except FileNotFoundError:
            print("File not found")