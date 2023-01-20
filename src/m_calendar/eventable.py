from fileManagement.buffer import BufferCreateI

class Eventable:
    """
    What this class can do:
    1) We can check if an event exists and get it's index from
        EventExists(self, event)
    
    2) We can get an event's index with
        GetEventIndex(self, event)
    
    ----- Those functions should be run recursively on all eventable objects -----
    eg from year add event -> add event to month -> add event to day
    eg from year remove enent -> remove event from month -> remove event from day
    
    3) We can add an event to the end of the events buffer and sort them with
        AddEvent(self, event)
        
    4) We can delete an event from the events buffer
       or delete an event at index from events buffer 
       DelEvent(self, event)
       DelEventAt(self, index)
    """
    def __init__(self):
        self.numEvents = 0
        self.events = None
        
    def GetEventAt(self, index):
        if(self.numEvents == 0):
            return
        
        return self.events.GetI(index)
        
    def EventExists(self, event):
        if(self.numEvents == 0):
            return
        """
        Returns index of event if it exists else it returns -1
        We get 2 features in 1 implementation
        
        1) We check if it returns -1 and we know if it exists
        2) We get it's index if it exists
        """
        for i in range(self.numEvents):
            if(event == self.events.GetI(i)):
                return i
        
        return -1
    
    def AddEvent(self, event):
        eventsBuffer = BufferCreateI(self.numEvents + 1)
        
        # copy old events to new Buffer
        if(self.numEvents != 0):
            for i in range(self.numEvents):
                eventsBuffer.SetI(i, self.events.GetI(i))
            
        
        # add new event
        self.numEvents += 1
        
        lastIndex = self.numEvents - 1
        
        eventsBuffer.SetI(lastIndex, event)    
        
        # copy new eventsBuffer to our old one
        
        self.events = BufferCreateI(self.numEvents)
        
        for i in range(self.numEvents):
            self.events.SetI(i, eventsBuffer.GetI(i))
            
        self.SortEvents()
        
    def DelEventAt(self, index):
        """
        Deletes event at index from events
        """
        if(self.numEvents == 0):
            return
        
        eventsBuffer = BufferCreateI(self.numEvents)
        
        # copy old events to new Buffer except the event at index
        
        for i in range(self.numEvents):
            # skip event at our specified index
            if(i == index):
                eventsBuffer.SetI(i, None)
                continue
            
            eventsBuffer.SetI(i, self.events.GetI(i))
            
        
        # remove event
        self.numEvents -= 1
        
        # copy new eventsBuffer to our old one
        
        if(self.numEvents == 0):
            self.events = None
            return
        
        self.events = BufferCreateI(self.numEvents)
        
        i = 0
        j = 0
        
        while(i < self.events.size and j < eventsBuffer.size):
            if(eventsBuffer.GetI(j) == None):
                j += 1
                continue
            
            self.events.SetI(i, eventsBuffer.GetI(j))
            
            i += 1
            j += 1
            
    def DelEvent(self, event):
        """
        Deletes event from events if it exists  
        """
        
        if(self.numEvents == 0):
            return
        
        index = self.EventExists(event)
        
        if(index == -1):
            # It Doesnt exist in events so we gut
            return
        
        self.DelEventAt(index)
            
    def GetEventIndex(self, event):
        if(self.numEvents == 0):
            return
        
        index = self.EventExists(event)
        
        return index
        
        
            
    def SortEvents(self):
        self.events.Sort()