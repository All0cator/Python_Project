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
        
        for i in range(len(eventsToFilter)):
            if(self.value == eventsToFilter.GetI(i).day):
                #add it to our events
                self.numEvents += 1
                self.events.Append(eventsToFilter.GetI(i))
                
    def GetDayIntervals(self):
        
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

"""     
    def AddEvent(self, event):
        
        super().AddEvent(event)
        
        \"""
        eventsBuffer = BufferCreateI(self.numEvents + 1)
        
        # copy old events to new Buffer
        
        for i in range(self.numEvents):
            eventsBuffer.SetI(i, self.events[i])
            
        
        # add new event
        self.numEvents += 1
        
        lastIndex = self.numEvents - 1
        
        eventsBuffer.SetI(lastIndex, event)    
        
        # copy new eventsBuffer to our old one
        
        self.events = BufferCreateI(self.numEvents)
        
        for i in range(self.numEvents):
            self.events.SetI(i, eventsBuffer.GetI(i))
            
        self.events.Sort()\"""
    
    def DelEvent(self, index):
        super().DelEvent(index)
        
"""