#from guardSettings import InitGuards

#InitGuards()

#from fileManagement.CSVFile import CSVFile

from m_calendar.calendRa import CalendRa
from fileManagement.buffer import Buffer, BufferCreateI, BufferCreateXY

from calendar import *

NUM_WEEK_DAYS = 7
NUM_MONTH_DAYS = 30
NUM_MONTHS = 12

class CalendR:
    
    #curMonth
    #curYear
    #events
    
    
    def __init__(self):
        return
    
    def GetMonth():
        return
    
    def GetYear():
        return
    
    
        
class Console:
    
    def __init__(self):
        
        self.calendar = CalendR()
        
        for row in range(5):
            for col in range(7):
                #copy day in curMonth calendar for display
                
                self.curMonthDays.append(calendar[row][col])
                
                # setup separators for curMonth for display
                
                self.curMonthDaysSeparators
        return
    
    def PrintLine(self):
        return
    
    pass



class Separators:
    
    #left
    #right
    #timesL
    #timesR
    
    def __init__(self, leftSeparator = " ", timesL = 1, rightSeparator = " ", timesR = 1):
        self.left = leftSeparator
        self.timesL = timesL
        self.right = rightSeparator
        self.timesR = timesR    
    pass

class YearDetails:
    
    def __init__(self):
        return
    

class MonthDetails:
    
    #monthDays
    #indexStart
    #numDays
    #
    
    def __init__(self, year, month):    
        tup = monthrange(year, month)

        self.year = year
        self.month = month
        self.indexStart = tup[0]
        self.numDays = tup[1]
            
class DayDetails:
    def __init__(self):
        return
        
def PreviousMonth(year, month):
    
    if(month == 1):
        newMonth = 12
        newYear = year - 1
    else:
        newMonth = month - 1
        newYear = year
    
    return (newYear, newMonth)

def NextMonth(year, month):
    
    if(month == 12):
        newMonth = 1
        newYear = year + 1
    else:
        newMonth = month + 1
        newYear = year
    
    return (newYear, newMonth)

def GetCalendar(year, month):
    calendR = monthcalendar(year, month)
    
    calendar = list()
    
    for row in calendR:
        for day in row:
            calendar.append(day)
            

    
    #Calendar Format Pipeline 
    
    args = (year, month)
    
    
    args = FormatCalendarDays(calendar, args)
    
    # args = FormatCalendarAddWeekHeader(calendar, args)
    
    #FormatCalendarDaysDecorations(calendar, args)
    
    return calendar
    
def FormatCalendarDays(calendar, args):
    
    year = args[0]
    month = args[1]
    
    #currentMonth = MonthDetails(year, month)
    tup = monthrange(year, month)
    
    monthStart = tup[0]
    monthLength = tup[1]
    
    tup = PreviousMonth(year, month)
    
    previousYear = tup[0]
    previousMonth = tup[1]
    
    
    tup = monthrange(previousYear, previousMonth)
    
    previousMonthDays = tup[1]
    
    tup = NextMonth(year, month)
    
    nextYear = tup[0]
    nextMonth = tup[1]
    
    tup = monthrange(nextYear, nextMonth)
    
    nextMonthDays = tup[1]
    
    j = 0
    
    i = 2
    
    while(j < 3):
        
        calendar[j] = ""
        
        if(previousMonthDays - i < 10):
            calendar[j] += " "
        
        calendar[j] += "   " + str(previousMonthDays - i) + " |"
        j += 1
        i -= 1 
    
    i = 1
    
    while(i <= monthLength):
        
        calendar[j] = ""
        
        calendar[j] += "[ "
        
        if(i < 10):
            calendar[j] += " "
        
        calendar[j] +=  str(i) + "] "
        
        
        if((j + 1) % 7 != 0):
            calendar[j] += "|"
        
        j += 1
        i += 1
        
    i = 1
    while(j < 35):
        
        calendar[j] = ""
        
        if(i < 10):
            calendar[j] += " "
        
        calendar[j] += "   " + str(i) + "  "
        i += 1
        j += 1

    buf = BufferCreateXY(7, 7)
    
    for y in range(5):
        for x in range(7):
            buf.SetXY(x, y, calendar[y*7 + x])
    
    x = 0
    for day in days:
        calendar.insert(x, "  " + day + " ")
        
        if(x % 6 != 0 or x == 0):
            calendar[x] += "|"
        
        x += 1
                    
    return args #+ (previousMonthDetails, nextMonthDetails)

days = ["ΔΕΥ", "ΤΡΙ", "ΤΕΤ", "ΠΕΜ", "ΠΑΡ", "ΣΑΒ", "ΚΥΡ"]   

def FormatCalendarDaysDecorations(calendar, args):
    #unpack arguments (args) tuple
    return


def PrintCalendar(calendaR):
    
    for x in range(calendaR.calendar.width):
        print(calendaR.daysHeader.GetI(x).GetText(), end="")
    
    print("\n")
    
    for y in range(calendaR.calendar.height):
        for x in range(calendaR.calendar.width):
            print(calendaR.calendar.GetXY(x, y).GetText(), end="") 
        print("\n")
    
    return

def main():    

    calendR = CalendRa()    

    while(True):
        i = input()
        if(i == 'q'):
            break
        
        if(i == 'a'): #left
            calendR.AdvanceMonth(CalendRa.DIRECTION_PREVIOUS)
            
            print("_____________________________________\n")
            print(CalendRa.months[calendR.currentMonth.value - 1] + "  " + str(calendR.currentMonth.year))
            print("_____________________________________\n")
            
            PrintCalendar(calendR)

        elif(i == 'd'): #right
            calendR.AdvanceMonth(CalendRa.DIRECTION_NEXT)
            
            print("_____________________________________\n")
            print(CalendRa.months[calendR.currentMonth.value - 1] + "  " + str(calendR.currentMonth.year))
            print("_____________________________________\n")
            
            PrintCalendar(calendR)
    
    return

main()