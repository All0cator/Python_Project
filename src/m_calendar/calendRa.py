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
from m_calendar.year import Year
from m_calendar.event import Event

from m_calendar.eventable import Eventable

class CalendRa(Eventable):
    
    months = ["ΙΑΝ", "ΦΕΒ", "ΜΑΡ", "ΑΠΡ", "ΜΑΙ", "ΙΟΥΝ", "ΙΟΥΛ", "ΑΥΓ", "ΣΕΠ", "ΟΚΤ", "ΝΟΕ", "ΔΕΚ"]
    days = ["ΔΕΥ", "ΤΡΙ", "ΤΕΤ", "ΠΕΜ", "ΠΑΡ", "ΣΑΒ", "ΚΥΡ"]
    
    NUM_WEEKDAYS = 7  
    
    DIRECTION_NEXT = 0
    DIRECTION_PREVIOUS = 1
    DIRECTIONS = {DIRECTION_NEXT, DIRECTION_PREVIOUS}
    
    # calendar is a list of days (Day)
    
    def __init__(self, startingYear=2022, startingMonth=12):
        
        #self.currentMonth = Month(startingYear, startingMonth)
        
        self.events = self.LoadEvents("..\\assets\\csvFiles\\events.csv")
        
        self.currentYear = Year(startingYear, startingMonth, self.events)
        
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
            
            event = Event(record)
            
            eventsBuffer.SetI(i - 1, event)
            
        
            
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
        
    def AddEvent(self, event):
        
        super().AddEvent(event)
        
        if(event.year == self.year):
            self.year.AddEvent(event)
        
    def DelEvent(self, event):
        
        index = self.EventExists(event)
        
        if(index == -1):
            return
        
        self.DelEventAt(index)
        
        super().DelEvent(event)
        
    def DelEventAt(self, index):
        
        eventToDelete = self.events.GetI(index)
        
        for i in range(self.numDays):
            
            index = self.days.GetI(i).EventExists(eventToDelete)
            
            if(index != -1):
                self.days.GetI(i).DelEvent(index)
                break
        
        super().DelEventAt(index)
        
    def GetDayOfYearMonth(self, year, month, day):
        
        year = Year(year, month, self.events)
        
        return year.currentMonth.days.GetI(day - 1)
        
    def GetEvents(self, year, month, day):
        
        year = Year(year, month, self.events)
        
        return year.currentMonth.days.GetI(day - 1).events
        
    
    def GetEventsText(self, year, month):
        
        # create the year, month, days 
        
        year = Year(year, month, self.events)
        
        selectedEvents = BufferCreateI(year.currentMonth.numEvents)
        
        for i in range(selectedEvents.size):
            selectedEvents.SetI(i, year.currentMonth.events.GetI(i))
        
        # now we have all events time to return a string like this
        # 0. [Event 1] -> Date: 2022-12-4, Time: 13:30, Duration: 30
        # 1. [Event 2] -> Date: 2022-12-5, Time: 13:45, Duration: 90
        # 2. [New Year's Eve] -> Date: 2022-12-31, Time: 23:59, Duration: 0
        # 3. [Christmas] -> Date: 2022-12-25, Time: 12:0, Duration: 60
        
        txt = ""
        
        for i in range(selectedEvents.size):
            leftSeparator = Separator(" " + str(i) + ". ")
            
            txt += leftSeparator + selectedEvents.GetI(i).ToText()
            
        return (txt, selectedEvents)
    
    def AdvanceMonth(self, direction):
        if(not direction in CalendRa.DIRECTIONS):
            assert(False and "Error: Wrong direction given for AdvanceMonth()")
            
        if(direction == CalendRa.DIRECTION_NEXT):
            
            nextMonth = self.currentYear.currentMonth.GetNextMonth()
            
            self.currentYear.currentMonth = nextMonth
            
            if(nextMonth.year != self.currentYear.value):
                
                nextYear = self.currentYear.GetNextYear()
                
                self.currentYear = nextYear
        else:
            previousMonth = self.currentYear.currentMonth.GetPreviousMonth()
            
            self.currentYear.currentMonth = previousMonth
            
            if(previousMonth.year != self.currentYear.value):
                
                previousYear = self.currentYear.GetPreviousYear()
                
                self.currentYear = previousYear
        
        self.UpdateCalendar()
        
    def UpdateCalendar(self):
        
        numWeeks = len(self.currentMonth.weeks)
        
        self.calendar = BufferCreateXY(CalendRa.NUM_WEEKDAYS, numWeeks)

        for x in range(CalendRa.NUM_WEEKDAYS):
            for y in range(numWeeks):
                self.calendar.SetXY(x, y, self.currentYear.weeks[y][x])
        
        j = 0
        i = self.currentYear.currentMonth.firstDayInWeekIndex - 1

        while(j < self.currentYear.currentMonth.firstDayInWeekIndex):
            
            leftSeparator = Separator()
            rightSeparator = Separator()
            
            if(self.currentYear.previousMonth.numDays - i < 10):
                print("Does this ever run?") # FLAG1
                leftSeparator.Append(" ")
            leftSeparator.Append("   ")    
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.ToText())
            
            
            self.calendar.GetI(j).value = self.currentYear.previousMonth.numDays - i
            
            
            rightSeparator.Append(" |")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.ToText())
            
            j += 1
            i -= 1 

        i = 1

        while(i <= self.currentYear.currentMonth.numDays):
            
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
    
    