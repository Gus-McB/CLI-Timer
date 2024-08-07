class Timer:
    def __init__(self, hour=0, minute=0, seconds=0):
        self.__hour = 0 
        self.__minute = 0
        self.__seconds = 0
        self.__total = int((self.__hour  * 3600) + (self.__minute  * 60) + self.__seconds )
        
    def setTime(self, time: list):
        self.__hour = int(time[0])
        self.__minute = int(time[1])
        self.__seconds = int(time[2])
        self.__total = (self.__hour * 3600) + (self.__minute * 60) + self.__seconds

    def getTotal(self):
        return self.__total
    
    def __repr__(self):
        return f"{self.__hour}:{self.__minute}:{self.__seconds}"  