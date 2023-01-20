from m_calendar.month import Month

from m_calendar.eventable import Eventable

from fileManagement.buffer import BufferCreateI

class Year(Eventable):
    def __init__(self, year, month, eventsToFilter):
        
        Eventable.__init__(self)
        
        self.value = year
        
        self.eventsToFilter = eventsToFilter
        if(eventsToFilter != None and eventsToFilter.size != 0):
            # count how many events are
            
            eventsList = list()
            
            for i in range(eventsToFilter.size):
                if(self.value == eventsToFilter.GetI(i).year):
                    #add it to our events
                    self.numEvents += 1
                    eventsList.append(eventsToFilter.GetI(i))
                    
            if(self.numEvents != 0):
                self.events = BufferCreateI(self.numEvents)
                
                for i in range(self.numEvents):
                    #add it to our events
                    self.events.SetI(i, eventsList[i])
            
        self.currentMonth = Month(year, month, self.events)
        
        previousMonthYear, previousMonth = self.currentMonth.GetPreviousMonth()
        self.previousMonth = Month(previousMonthYear, previousMonth, self.eventsToFilter)
        
        nextMonthYear, nextMonth = self.currentMonth.GetNextMonth()
        self.nextMonth = Month(nextMonthYear, nextMonth, self.eventsToFilter)
        
    def GetPreviousYear(self):
        
        if(self.value > 1):
            return self.value - 1
        else:
            return self.value

    def GetNextYear(self):
        
        if(self.value < 9999):
            return self.value + 1
        else:
            return self.value
        
    def AddEvent(self, event):
        super().AddEvent(event)
        
        if(event.month == self.currentMonth.value):
            self.currentMonth.AddEvent(event)
        
    def DelEvent(self, event):
        
        if(self.numEvents == 0):
            return
        
        index = self.EventExists(event)
        
        if(index == -1):
            return
        
        self.DelEventAt(index)
    
    def DelEventAt(self, index):
        
        if(self.numEvents == 0):
            return
        
        eventToDelete = self.events.GetI(index)
        
        if(self.currentMonth.EventExists(eventToDelete)):
            self.currrentMonth.DelEvent()
        
        
        super().DelEvent(index)
        