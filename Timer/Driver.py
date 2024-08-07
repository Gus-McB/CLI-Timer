import Clock, Agenda, time, task, CSV

class Drive:
    def __init__(self):
        self.CSVAccess = CSV.CSVAccess(None)
        
    def run(self): #The main timer function that takes all classes that require a input into use. After the user makes their selctions the timer will start.
        self.agenda = Agenda.Agendas()
        print("\nWould you like to import a timer (csv)? [y/n]:")
        user = input("> ").lower()
        while user != "y" and user != "n":
            print("\nPlease choose a valid input [y/n]:")
            user = input("> ").lower()
    
        if user == 'y':
            print("\nWhat file would you like to use: ")
            fileName = input("> ")
            try: # Prevents incorrect file  names.
                self.CSVAccess.fileName = fileName
                csvTasks = self.CSVAccess.timeImport(fileName)
                index = 0
                for task in csvTasks:
                    times = task[1].split(':')
                    self.agenda.addTask(task[0])
                    self.agenda.getAgenda()[index].timer.setTime(times)
                    index += 1
            except:
                print("File not found.")
                self.run()
            self.agenda.start()
            
        print("\nWould you like to use a preset? [y/n]")
        user = input("> ").lower()
        if user == "y":
            while user != "y" and user != "n":
                print("\nPlease choose a valid input [y/n]:")
            print("\nSelect which format you want:")
            preset1 = CSV.CSVAccess("preset1")
            preset2 = CSV.CSVAccess("preset2")
            preset3 = CSV.CSVAccess("preset3")
            print("1: ", preset1.timeImport("preset1"))
            print("2: ", preset2.timeImport("preset2"))
            print("3: ", preset3.timeImport("preset3"))
            self.agenda.preset()
            self.agenda.start()

        elif user == 'n':
            print("\nInput all the names for your tasks separated by ','.")
            user = input("> ")

            taskList = user.split(",") #splits the task ,
            for taskName in taskList: #sends the task to the add task method
                self.agenda.addTask(taskName)

            self.agenda.timeAllocation()
            self.agenda.taskList()
            userEdit = "n"
            while userEdit == "n":
                print("Would you like to continue with this timer? [y/n]:")
                userEdit = input("> ").lower()
                while userEdit != "y" and userEdit != "n":
                    print("Please use a valid input.")
                    user = input("> ").lower()
                if userEdit == "n":
                    print("\nSelect the task you want to edit: ")
                    user = input("> ").lower()
                    print("\nIf you wish to delete a task assign it a '0' time value.")
                    print("Choose a new time, 'H:MM:SS': ")
                    newTime = input("> ").split(":")
                    try:
                        self.agenda.edit(user, newTime)
                        self.agenda.taskList()
                    except:
                        print("not a valid task.")
            self.agenda.start()

d = Drive()

print("Would you like to begin? [y/n]")
user = input("> ").lower()
while user != "y" and user != "n":
    print("Please choose a valid input [y/n]:")
    user = input("> ").lower()
if user == "y":
    while user == "y":
        d.run()
        print("All timers have finshed would you like to add more timers [y/n]")
        user = input("> ").lower()

print("Thanks for using our timer")