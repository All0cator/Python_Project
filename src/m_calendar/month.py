from calendar import monthcalendar, monthrange

class Month:
    def __init__(self, year, month):
        
        self.value = month
        self.year = year
        
        self.weeks = monthcalendar(year, month)
        
        tup = monthrange(year, month)
    
        self.firstDayInWeekIndex = tup[0]
    
        self.numDays = tup[1]
        
        self.events = None
        self.numEvents = 0
        
    def GetPreviousMonth(self):
        
        month = self.value
        year = self.year
        
        if(month == 1):
            month = 12
            year = year - 1
        else:
            month = month - 1
            # self.year doesnt change
            
        return Month(year, month)

    def GetNextMonth(self):
        
        month = self.value
        year = self.year
        
        if(month == 12):
            month = 1
            year = year + 1
        else:
            month = month + 1
            # year doesnt change
        
        return Month(year, month)