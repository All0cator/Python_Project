
class Interval:
    def __init__(self, hour, mins, duration):
        """
        duration is in minutes or else doesnt work
        """
        self.hour = hour
        self.mins = mins
        self.duration = duration
        
        self.startMins = mins
        self.startHour = hour
        
        self.startHourMin = ":".join([self.startHour, self.startMins])
        
        self.endMins = (self.startMins + duration) % 60
        
        self.endHour = self.startHour + (self.startMins + duration) // 60
        
        self.endHour %= 24
        
        self.endHourMin = ":".join([self.endHour, self.endMins])
        
        self.startMinuteStamp = self.startMins + self.startHour * 60
        self.endMinuteStamp = self.startMinuteStamp + duration
        
    def ToText(self):
        return "({0}) - ({1})".format(self.startHourMin, self.endHourMin)
    