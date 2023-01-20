from m_calendar.separator import Separator
from fileManagement.buffer import BufferCreateI

from m_calendar.interval import Interval

from m_calendar.eventable import Eventable

class Day(Eventable):
    def __init__(self, day, eventsToFilter, textLeftSeparator="", textRightSeparator=""):
        Eventable.__init__(self)
        
        self.value = day
        self.leftSeparator = Separator(textLeftSeparator)
        self.rightSeparator = Separator(textRightSeparator)
        
        # count how many events are
        
        if(eventsToFilter != None):
            if(eventsToFilter.size != 0):
                eventsList = list()
                
                for i in range(eventsToFilter.size):
                    if(self.value == eventsToFilter.GetI(i).day):

                        #add it to our events
                        self.numEvents += 1
                        eventsList.append(eventsToFilter.GetI(i))
                        
            

                if(self.numEvents != 0):
                    self.events = BufferCreateI(self.numEvents)
                
                    for i in range(self.numEvents):
                        #add it to our events
                        self.events.SetI(i, eventsList[i])
                
    def GetDayIntervals(self):
        if(self.numEvents == 0):
            intervals = BufferCreateI(1)
            intervals.SetI(0, Interval(0, 0, 1440))
            
            return intervals
        
        intervals = BufferCreateI(self.numEvents)
        
        for i in range(self.numEvents):
            curEvent = self.events.GetI(i)
        
            interval = Interval(curEvent.hour, curEvent.minutes, curEvent.Get("Duration"))
            
            intervals.SetI(i, interval)
            
        return intervals
            
            
            
        
    def ToText(self):
        if(self.numEvents > 0):
            self.leftSeparator.ReplaceEndCharacterWith("*")
        
        return self.leftSeparator.ToText() + str(self.value) + self.rightSeparator.ToText()