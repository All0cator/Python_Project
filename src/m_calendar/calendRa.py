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

from calendar import *

from fileManagement.buffer import Buffer, BufferCreateI, BufferCreateXY

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
        
        self.daysHeader = BufferCreateI(CalendRa.NUM_WEEKDAYS)
        
        x = 0
        for day in CalendRa.days:
            self.daysHeader.SetI(x, Day(day,"  ", " "))
            
            if(x % 6 != 0 or x == 0):
                self.daysHeader.GetI(x).rightSeparator.Append("|")
            
            x += 1
            
        self.UpdateCalendar()
    
    def AdvanceMonth(self, direction):     
        if(not direction in CalendRa.DIRECTIONS):
            assert(False and "Error: Wrong direction given for AdvanceMonth()")
        
        if(direction == CalendRa.DIRECTION_NEXT):
            self.currentMonth = self.currentMonth.GetNextMonth()
        else:
            self.currentMonth = self.currentMonth.GetPreviousMonth()
        
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
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.text)
            
            
            self.calendar.GetI(j).value = self.previousMonth.numDays - i
            
            
            rightSeparator.Append(" |")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.text)
            
            j += 1
            i -= 1 

        i = 1

        while(i <= self.currentMonth.numDays):
            
            leftSeparator = Separator()
            rightSeparator = Separator()
            
            leftSeparator.Append("[ ")
            if(i < 10):
                leftSeparator.Append(" ")
            
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.text)
            
            
            self.calendar.GetI(j).value = i
            
            
            rightSeparator.Append("] ")
            if((j + 1) % 7 != 0):
                rightSeparator.Append("|")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.text)
            
            j += 1
            i += 1
            
        i = 1
        while(j < self.calendar.size):
            
            leftSeparator = Separator()
            rightSeparator = Separator()
            
            if(i < 10):
                leftSeparator.Append(" ")
            leftSeparator.Append("   ")
            self.calendar.GetI(j).leftSeparator.Append(leftSeparator.text)
            
            
            self.calendar.GetI(j).value = i
            
            
            rightSeparator.Append("  ")
            self.calendar.GetI(j).rightSeparator.Append(rightSeparator.text)
            
            i += 1
            j += 1
        
class Month:
    def __init__(self, year, month):
        
        self.value = month
        self.year = year
        
        self.weeks = monthcalendar(year, month)
        
        tup = monthrange(year, month)
    
        self.firstDayInWeekIndex = tup[0]
    
        self.numDays = tup[1]
        
    def GetPreviousMonth(self):
        
        month = self.value
        year = self.year
        
        if(month == 1):
            month = 12
            year = year - 1
        else:
            month = month - 1
            # self.year doesnt change
            
        return Month(year, month)

    def GetNextMonth(self):
        
        month = self.value
        year = self.year
        
        if(month == 12):
            month = 1
            year = year + 1
        else:
            month = month + 1
            # year doesnt change
        
        return Month(year, month)
    
class Day:
    def __init__(self, value, textLeftSeparator="", textRightSeparator=""):
        self.value = value
        self.leftSeparator = Separator(textLeftSeparator)
        self.rightSeparator = Separator(textRightSeparator)
        
    def GetText(self):
        return self.leftSeparator.text + str(self.value) + self.rightSeparator.text

class Separator:
    def __init__(self, text="", isALine=False):
        self.text = text
        self.isALine = isALine
    
    def Append(self, value):
        if(self.isALine):
            assert(False and "Error: Cannot append more text in a line.")
        
        self.text += value