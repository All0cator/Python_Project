from m_calendar.separator import Separator
from fileManagement.buffer import BufferCreateI

class Day:
    def __init__(self, value, textLeftSeparator="", textRightSeparator=""):
        self.value = value
        self.leftSeparator = Separator(textLeftSeparator)
        self.rightSeparator = Separator(textRightSeparator)
        self.events = None
        self.numEvents = 0
        
    def ToText(self):
        if(self.numEvents > 0):
            self.leftSeparator.ReplaceEndCharacterWith("*")
        
        return self.leftSeparator.ToText() + str(self.value) + self.rightSeparator.ToText()
    
    def AddEvent(self, event):
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
            
        self.events.Sort()
    