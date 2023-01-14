# shmantikh shmeiosh to hmerologio pou periexei tis hmeres einai sthn ousia 6 grammes 7 sthles
# giati an enas mhnas arxizei apo thn kyriakh kai exei 30 hmeres exoume to parakato

# (etsi einai h morfh tou calendar tou programmatos)

# ΔΕΥ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ

#  25 |   26 |   27 |   28 |   29 |   30 |[  1]

#[  2] |[  3] |[  4] |[  5] |[  6] |[  7] |[  8]

#[  9] |[ 10] |[ 11] |[ 12] |[ 13] |[ 14] |[ 15]

#[ 16] |[ 17] |[ 18] |[ 19] |[ 20] |[ 21] |[ 22]

#[ 23] |[ 24] |[ 25] |[ 26] |[ 27] |[ 28] |[ 29]

#[ 30] |    1      2      3      4      5      6

from fileManagement.buffer import BufferCreateI, BufferCreateXY
from fileManagement.CSVFile import CSVFile
from m_calendar.separator import Separator
from m_calendar.month import Month
from m_calendar.day import Day


class CalendRa:
    
    months = ["ΙΑΝ", "ΦΕΒ", "ΜΑΡ", "ΑΠΡ", "ΜΑΙ", "ΙΟΥΝ", "ΙΟΥΛ", "ΑΥΓ", "ΣΕΠ", "ΟΚΤ", "ΝΟΕ", "ΔΕΚ"]
    days = ["ΔΕΥ", "ΤΡΙ", "ΤΕΤ", "ΠΕΜ", "ΠΑΡ", "ΣΑΒ", "ΚΥΡ"]
    
    NUM_WEEKDAYS = 7  
    
    DIRECTION_NEXT = 0
    DIRECTION_PREVIOUS = 1
    DIRECTIONS = {DIRECTION_NEXT, DIRECTION_PREVIOUS}
    
    # calendar is a list of days (Day)
    
    def __init__(self, startingYear=2022, startingMonth=12):
        
        self.currentMonth = Month(startingYear, startingMonth)
        
        self.events = self.LoadEvents("assets/csvFiles/events.csv")
        
        self.daysHeader = BufferCreateI(CalendRa.NUM_WEEKDAYS)
        
        x = 0
        for day in CalendRa.days:
            self.daysHeader.SetI(x, Day(day,"  ", " "))
            
            if(x % 6 != 0 or x == 0):
                self.daysHeader.GetI(x).rightSeparator.Append("|")
            
            x += 1
            
        self.UpdateCalendar()
    
    def LoadEvents(self, path):
        file = CSVFile(path)
        
        eventsBuffer = BufferCreateI(file.numRows)
        
        self.numEvents = 0
        
        self.header = file.GetHeader()
        
        for i in range(1, file.numRows):
            record = file.GetNthRecord(i)
            
            self.numEvents += 1
            
            # unpacking record
            
            
            
            eventsBuffer.SetI(i, Event(record.))
            
    def SaveEvents(self, path):
        file = CSVFile(path)
        
        dataToSave = BufferCreateI(self.numEvents)
        
        for i in range(self.numEvents):
            dataToSave.SetI(i, self.events.GetI(i).ToCSVLine())
        
        #clear file
        emptyBuffer = BufferCreateI(1)
        emptyBuffer.SetI(0, "")
        
        file.WriteFile("w", emptyBuffer)
        
        
        
        file.WriteFile("w", dataToSave)
        
    def AddEvent(self, event, day):
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
    
    def CSVToEvent():
        
    
    def GetEvents(self, year, month):
        
        selectedEvents = BufferCreateI
        
        for i in range(self.numEvents):
            self.events.GetI(i)
        
    
    def AdvanceMonth(self, direction):     
        if(not direction in CalendRa.DIRECTIONS):
            assert(False and "Error: Wrong direction given for AdvanceMonth()")
        
        if(direction == CalendRa.DIRECTION_NEXT):
            self.currentMonth = self.currentMonth.GetNextMonth(self.events)
        else:
            self.currentMonth = self.currentMonth.GetPreviousMonth(self.events)
        
        self.UpdateCalendar()    
        
    def UpdateCalendar(self):
        
        numWeeks = len(self.currentMonth.weeks)
        
        self.calendar = BufferCreateXY(CalendRa.NUM_WEEKDAYS, numWeeks)

        for x in range(CalendRa.NUM_WEEKDAYS):
            for y in range(numWeeks):
                self.calendar.SetXY(x, y, Day(self.currentMonth.weeks[y][x]))
        
        self.previousMonth = self.currentMonth.GetPreviousMonth()
        self.nextMonth = self.currentMonth.GetNextMonth()
        
        j = 0
        i = self.currentMonth.firstDayInWeekIndex - 1

        while(j < self.currentMonth.firstDayInWeekIndex):
            
            leftSeparator = Separator()
            rightSeparator = Separator()
            
            
            if(self.previousMonth.numDays - i < 10):
                leftSeparator.Append(" ")
            leftSeparator.Append("   ")    
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.ToText())
            
            
            self.calendar.GetI(j).value = self.previousMonth.numDays - i
            
            
            rightSeparator.Append(" |")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.ToText())
            
            j += 1
            i -= 1 

        i = 1

        while(i <= self.currentMonth.numDays):
            
            leftSeparator = Separator()
            rightSeparator = Separator()
            
            leftSeparator.Append("[ ")
            if(i < 10):
                leftSeparator.Append(" ")
            
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.ToText())
            
            
            self.calendar.GetI(j).value = i
            
            
            rightSeparator.Append("] ")
            if((j + 1) % 7 != 0):
                rightSeparator.Append("|")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.ToText())
            
            j += 1
            i += 1
            
        i = 1
        while(j < self.calendar.size):
            
            leftSeparator = Separator()
            rightSeparator = Separator()
            
            if(i < 10):
                leftSeparator.Append(" ")
            leftSeparator.Append("   ")
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.ToText())
            
            
            self.calendar.GetI(j).value = i
            
            
            rightSeparator.Append("  ")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.ToText())
            
            i += 1
            j += 1
    
    