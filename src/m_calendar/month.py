from calendar import monthcalendar, monthrange

from m_calendar.eventable import Eventable

from fileManagement.buffer import BufferCreateI

from m_calendar.day import Day

class Month(Eventable):
    def __init__(self, year, month, eventsToFilter):

        Eventable.__init__(self)
        
        self.value = month
        
        self.year = year
        self.eventsToFilter = eventsToFilter
        
        if(eventsToFilter != None and eventsToFilter.size != 0):
            # count how many events are
            
            eventsList = list()
            
            for i in range(eventsToFilter.size):
                if(self.value == eventsToFilter.GetI(i).month and self.year == eventsToFilter.GetI(i).year):

                    #add it to our events
                    self.numEvents += 1
                    eventsList.append(eventsToFilter.GetI(i))
            
            if(self.numEvents != 0):
            
                self.events = BufferCreateI(self.numEvents)
            
                for i in range(self.numEvents):
                    #add it to our events
                    self.events.SetI(i, eventsList[i])
        
        
        self.weeks = monthcalendar(year, month)
        
        tup = monthrange(year, month)
    
        self.firstDayInWeekIndex = tup[0]
    

        self.numDays = tup[1]
        
        self.days = BufferCreateI(self.numDays)
        
        self.CreateDays()
        
    def CreateDays(self):
        for i in range(self.numDays):
            self.days.SetI(i, Day(i + 1, self.events if self.events != None else None))
            
    def GetPreviousMonth(self):
        
        month = self.value
        year = self.year
        
        if(month == 1):
            month = 12
            year = year - 1
        else:
            month = month - 1
            # self.year doesnt change
            
        return (year, month)

    def GetNextMonth(self):
        
        month = self.value
        year = self.year
        
        if(month == 12):
            month = 1
            year = year + 1
        else:
            month = month + 1
            # year doesnt change
        
        return (year, month)
    
    def AddEvent(self, event):
        super().AddEvent(event)
        
        for i in range(self.numDays):
            if(self.days.GetI(i).value == event.day):
                self.days.GetI(i).AddEvent(event)
                break

    def DelEvent(self, event):
        
        if(self.numEvents == 0):
            return
        
        index = self.EventExists(event)
        
        if(index == -1):
            return
        
        self.DelEventAt(index)
        
        super().DelEvent(event)
    
    def DelEventAt(self, index):
        
        if(self.numEvents == 0):
            return
        
        eventToDelete = self.events.GetI(index)
        
        for i in range(self.numDays):
            
            index = self.days.GetI(i).EventExists(eventToDelete)
            
            if(index != -1):
                self.days.GetI(i).DelEvent(index)
                break
        
        super().DelEventAt(index)
        