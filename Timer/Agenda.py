import Clock, time, datetime, CSV
from task import Task
from playsound import playsound
from CSV import CSVAccess

class Agendas:
    def __init__(self):
        self.__agenda = []
        self.timeInput = []

    def getAgenda(self):
        return self.__agenda

    def addTask(self, taskName): #add tasks to the list
        while isinstance(taskName, str) != True:
            print("Choose a valid String:")
            taskName = input("> ")
        self.__agenda.append(Task(taskName))

    def timeAllocation(self): #Allocates how much time they would like to spend on each task in the agenda list.
        for task in self.__agenda:
            print("\nHow much time would you like to allocate for the task '" + task.name +
                    "' (H:MM:SS).")
            time = input("> ")
            timeSplit = time.split(":")
            self.timeInput.append(time)
            try:
                task.timer.setTime(timeSplit)
            except:
                print("These are not valid times, remember 'H:MM:SS'.")
                self.timeAllocation()

    def removeTask(self, name): #removes task from the list.
        for i in self.__agenda:
            if i.name == name:
                self.__agenda.remove(i)

    def calcEndTime(self): #calculates the end time of the timer using the current time. 
        total = 0
        for i in self.__agenda:
            total += i.timer.getTotal()
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=total)
        return format(endTime, '%H:%M:%S')
    
    def preset(self): #Allows the user to select a preset timer.
        preset = input("\nPlease select your preset file: \n")
        if preset == "1":
            preset = "preset1"
        elif preset == "2":
            preset = "preset2"
        elif preset == "3":
            preset = "preset3"
        else:
            print("Not a valid preset.")
            self.preset()

        try:
            csv = CSVAccess(preset)
            csv.importTask()
            print("\nThis is your selected meeting format would you like to continue? [y/n]:")
            confirm = input("> ").lower()
            while confirm != "y" and confirm != "n":
                print("Please use a valid input.")
                confirm = input("> ").lower()
            if confirm == "y":
                csvTask = csv.timeImport(preset)
                for i in csvTask:
                    taskName = i[0]
                    taskTime = i[1]
                    self.addTask(taskName)
                    hours, minutes, seconds = csv.Time(taskTime)
                    self.timeInput.append(taskTime)
                    self.__agenda[-1].timer.setTime((hours, minutes, seconds))
                print("Timer is ready")
        except:
            print("File not found")

    def taskList(self): #Counts the tasks in the list and displays them to the terminal.
            count = 1
            print("Agenda list")
            print("-------------------------------------------")
            for task in self.__agenda:
                print(f"{count}. {task.name} {task.timer}")
                count += 1
            print("-------------------------------------------")

    def edit(self, name, time: list): #Allows the user to edit tasks that have been added to the list. 
        for task in self.__agenda:
            if task.name == name:
                if len(time) > 1:
                    task.timer.setTime(time)
                else:
                    self.removeTask(name)

    def start(self): #Starts the main timer with the tasks that have been added to the list.
        print(f"\nThe end time will be {self.calcEndTime()}\n")
        print("Press Enter to start the agenda")
        input()# if the user presses enter starts the timer
        lastTask = self.__agenda[-1].name
        for task in self.__agenda: #loops through all the task
            
            skip = False 
            total = task.timer.getTotal()#gets the total for the Timer

            print(f"\n{task.name} is about to begin.")
            print("")
            print(f"Pause timer Ctrl + C ")
            playsound("sounds/start.mp3")
            while total > 0 and skip == False:
                try:
                    timer = datetime.timedelta(seconds = total)
                    print(f"Task: {task.name}, Time left: {timer}", end="\r")
                    time.sleep(1)
                    total -= 1 #updates the timer every second
                    
                except KeyboardInterrupt:#stops the timer
                    playsound("sounds/pause.mp3")
                    print(f"You paused the task {task.name} at {timer}, what would you like to do? Play/Skip/Advance/Edit") #options for the timer
                    options = input("> ").strip().lower()
                    while options != "skip" and options != "play" and options != "edit" and options != "advance":
                        print("please use a valid input.")
                        options = input("> ").strip().lower()

                    if options == "skip": #skips the task
                        skip = True
                    elif options == "play":#unpause
                        playsound("sounds/start.mp3")
                    elif options == "advance":#allows user to edit the time on the current task
                        print(f"What would you like the timer changed to? ")
                        options = input("> ").split(":")
                        task.timer.setTime(options)
                        total = task.timer.getTotal()

                    elif options == "edit":#to update task list
                        print("Change Task Name = Name \nRemove a task = remove \nAdd task = Add \nExit ")
                        user = input("> ").strip().lower()
                        while user != "name" and user != "remove" and user != "add" and user != "exit":
                            print("please use a valid input.")
                            user = input("> ").strip().lower()

                        if user == "exit":
                            pass
                        
                        if user == "name":#task name
                            self.taskList()
                            print("Enter which Task you would like to change \n")
                            taskNum = int(input("> "))-1
                            while taskNum <= 0 and taskNum > len(self.__agenda):#making sure that the entered task is in the list
                                print("please use a valid input.")
                                taskNum = int(input("> "))-1

                            print("Enter new name")
                            newName = input("> ")
                            self.__agenda[taskNum].name = newName
                            self.taskList()

                       
                        # elif user == "time": #allows the user to change the time of diffrent agendas
                        #     self.taskList()
                    
                        #     print("Enter which Task you would like to change \n")
                        #     taskNum1 = int(input(">"))-1
                        #     while taskNum1 <= 0 and taskNum1 > len(self.__agenda):#making sure that the entered task is in the list
                        #         print("please use a valid input.")
                        #         taskNum1 = int(input("> "))-1                            

                        #     print("Enter the updated time for the task '" + self.__agenda[taskNum1].name +
                        #             "' (H:MM:SS).")
                        #     options1 = input("> ").split(":")
                        #     self.__agenda[taskNum1].timer.setTime(options1)
                        #     self.taskList()
                        
                        elif user == "remove":#adding a task to the list
                            self.taskList()

                            print("Enter the name of the task you would like to remove: ")
                            taskName = input("> ")

                            if taskName == task.name:
                                skip = True
                            try:
                                self.removeTask(taskName)
                            except ValueError:
                                print("This is not a valid task, try again.\n")
                            self.taskList()

                        elif user == "add":#adds a task to the adgenda
                            print("Enter Task Name")
                            options = input("> ")

                            self.addTask(options)
                            lL = len(self.__agenda)-1
                            print("How much time would you like to allocate for the task '" + options +
                                    "' (H:MM:SS).")
                            time1 = input("> ")
                            timeSplit = time1.split(":")
                            self.timeInput.append(time1)
                            self.__agenda[lL].timer.setTime(timeSplit)
                            self.taskList()
    
                            
            if task.name == lastTask:
                playsound("sounds/last_task.mp3")
            elif total == 0:
                playsound("sounds/task_finished.mp3")
                        
            print(f"\n{task.name} has finished")
            if self.__agenda[-1].name == task.name: #if there are timers left it will say next task is about to begin
                pass
            else:
                print("Next Task is about to begin ")

        choice = 'n'
        print("Would you like to export this file? [y/n]:")
        choice = input("> ")

        if choice == 'y':
            print("Name this file:")
            name = input("> ")
            access = CSV.CSVAccess(name)
            nameList = []
            if len(nameList) >= 0:
                for i in self.__agenda:
                    nameList.append(i.name)
                access.exportTasks(nameList, self.timeInput)
            choice = "n"
        else:
            pass
        print("\n")
        print("Agenda finished. Returning to the main menu...")#once all the timers are finshed

