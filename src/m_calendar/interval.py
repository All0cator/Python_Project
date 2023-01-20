
class Interval:
    def __init__(self, hour, mins, duration):
        """
        duration is in minutes or else doesnt work
        """
        
        
        self.hour = int(hour)
        self.mins = int(mins)
        self.duration = duration
        
        self.startMins = self.mins
        self.startHour = self.hour
        
        self.startHourMin = ":".join([str(self.startHour), str(self.startMins)])
        
        self.endMins = (self.startMins + self.duration) % 60
        
        self.endHour = self.startHour + (self.startMins + self.duration) // 60
        
        self.endHour %= 24
        
        self.endHourMin = ":".join([str(self.endHour), str(self.endMins)])
        
        self.startMinuteStamp = self.startMins + self.startHour * 60
        self.endMinuteStamp = self.startMinuteStamp + self.duration
        
    def ToText(self):
        return "({0}) - ({1})".format(self.startHourMin, self.endHourMin)
    