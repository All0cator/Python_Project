from datetime import *
from m_calendar.eventAttribute import EventAttribute

ATTRIBUTE_NAMES = ["Date", "Hour", "Duration", "Title"]
NUM_ATTRIBUTE_NAMES = 4

TIME_ATTRIBUTE_NAMES = ["Date", "Hour", "Duration"]
NUM_TIME_ATTRIBUTE_NAMES = 3

class Event:
    """
    
    """
    
    def __init__(self, attributes, titleBoard=["[", "]"], pointer="->"):
        
        if(len(attributes) != ATTRIBUTE_NAMES):
            assert(False and "Error: Event given not enough attributes!")
        
        for i in range(len(attributes)):
            # dictionary with keys ATTRIBUTE_NAMES and values attributes
            if(attributes[i].isdigit()):
                self.attributes[ATTRIBUTE_NAMES[i]] = EventAttribute(int(attributes[i]))
            else:
                self.attributes[ATTRIBUTE_NAMES[i]] = EventAttribute(attributes[i])
        
        self.Update(titleBoard, pointer)
    
    # Using get for syntactical sugar
    # self.attributes["Date"] vs self.Get("Date") syntax
    
    def OverlapsWith(self, event):
        """
        """
        
        eventEndsBetweenOtherEvent = event.end > self.start and event.end <= self.end
        eventBeginsBetweenOtherEvent = event.start >= self.start and event.start < self.end
        
        if((eventEndsBetweenOtherEvent or eventBeginsBetweenOtherEvent) and event.date == self.date):
            return True
        
        return False
    
        # Yes i could return eventEndsBetweenOtherEvent or eventBeginsBetweenOtherEvent but the way i did it was more clear to the reader
    
    def OverlapsWithOtherEvents(self, events):
        for i in range(events.size):
            if(self.OverlapsWith(events.GetI(i))):
                return True
            
        return False
    
    def Set(self, attributeName, value):
        # The reason \n is used in docstring bellow is to make each attribute appear on its own line when hovering on Get
        
        """
        ATTRIBUTE_NAMES : 
            "Date"             eg 2022-11-25\n
            "Hour"             eg 10:50\n
            "Duration"     eg 90\n
            "Title"           eg Python Lesson\n
        """
        
        self.attributes[attributeName].val = value
        
        # i dont care about performance after i change one of the event's attributes i update everything
        self.Update()
        
    def Update(self, titleBoard=["[", "]"], pointer="->"):
        
        self.titleBoard = titleBoard
        self.pointer = pointer
        
        year, month, day = self.Get("Date").split("-")
        
        self.date = datetime.date(year, month, day)
        self.hour, self.minutes = self.Get("Hour").split(":")
        
        self.start = self.hour*60 + self.minutes
        self.end = self.start + self.Get("Duration")

        self.title = self.Get("Title")
        
        self.titleBoard = titleBoard
        self.pointer = pointer
    
    def Get(self, attributeName):
        
        # The reason \n is used in docstring bellow is to make each attribute appear on its own line when hovering on Get
        
        """
        ATTRIBUTE_NAMES : 
            "Date"             eg 2022-11-25\n
            "Hour"             eg 10:50\n
            "Duration"     eg 90\n
            "Title"           eg Python Lesson\n
        """
        if(not attributeName in self.attributes.keys()):
            assert(False and f"Error: atribute name {attributeName} not found in dictionary")
        
        return self.attributes[attributeName].val
    
    def ToCSVLine(self):
        line = ""
        
        for i in range(NUM_ATTRIBUTE_NAMES - 1):
            line += self.Get(ATTRIBUTE_NAMES[i]) + ","
            
        finalIndex = NUM_ATTRIBUTE_NAMES - 1
        line += ATTRIBUTE_NAMES[finalIndex]
        
        return line
        
    def ToText(self):
        text = ""
        
        # [Event 1] -> Date: 2022-12-4, Time: 13:30, Duration: 30
        # delimeter: , 
        # pointer: ->
        # titleBoard = []
        text += self.titleBoard[0] + self.title + self.titleBoard[1] + " " + self.pointer + " "

        for i in range(NUM_ATTRIBUTE_NAMES):
            text += self.attributes[ATTRIBUTE_NAMES[i]].ToText()
    
    # Compare two Events only by their time(date and hour) duration and title doesnt affect comparisons
    
    # override < operator for Event object
    def __lt__(self, other):
        
        i = 0
        
        while(i < NUM_TIME_ATTRIBUTE_NAMES):
            if(self.Get(TIME_ATTRIBUTE_NAMES[i]) < other.Get(TIME_ATTRIBUTE_NAMES[i])):
                return True
            
            i += 1
        
        return False
    
    # override == operator for Event object
    def __eq__(self, other):
        i = 0
        
        while(i < NUM_TIME_ATTRIBUTE_NAMES):
            if(self.Get(TIME_ATTRIBUTE_NAMES[i]) != other.Get(TIME_ATTRIBUTE_NAMES[i])):
                return False
            
            i += 1
        
        return True
        
    
    # override != operator for Event object
    def __ne__(self, other):
        return not self == other
    
    # override > operator for Event object
    def __gt__(self, other):
        return other < self
    
    # override <= operator for Event object
    def __le__(self, other):
        return self < other or self == other
    
    # override >= operator for Event object
    def __ge__(self, other):
        return self > other or self == other
    
    
