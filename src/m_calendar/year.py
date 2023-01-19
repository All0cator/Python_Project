from m_calendar.month import Month

from m_calendar.eventable import Eventable

class Year(Eventable):
    def __init__(self, year, month, eventsToFilter):
        
        Eventable.__init__(self)
        
        self.value = year
        
        for i in range(len(eventsToFilter)):
            if(self.value == eventsToFilter.GetI(i).year):
                #add it to our events
                self.numEvents += 1
                self.events.Append(eventsToFilter.GetI(i))
        
        self.currentMonth = Month(year, month, self.events)
        self.previousMonth = self.currentMonth.GetPreviousMonth()
        self.nextMonth = self.currentMonth.GetNextMonth()
        
    def GetPreviousYear(self):
        
        if(self.value > 1):
            return Year(self.value - 1, self.currentMonth.value, self.events)
        else:
            return Year(self.value, self.currentMonth.value, self.events)

    def GetNextYear(self):
        
        if(self.value < 9999):
            return Year(self.value + 1, self.currentMonth.value, self.events)
        else:
            return Year(self.value, self.currentMonth.value, self.events)
        
    def AddEvent(self, event):
        super().AddEvent(event)
        
        if(event.month == self.currentMonth.value):
            self.currentMonth.AddEvent(event)
        
    def DelEvent(self, event):
        
        index = self.EventExists(event)
        
        if(index == -1):
            return
        
        self.DelEventAt(index)
    
    def DelEventAt(self, index):
        
        eventToDelete = self.events.GetI(index)
        
        if(self.currentMonth.EventExists(eventToDelete)):
            self.currrentMonth.DelEvent()
        
        
        super().DelEvent(index)
        