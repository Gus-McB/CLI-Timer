from Clock import Timer 

class Task:
    def __init__(self, name):
        self.name = name
        self.timer = Timer()