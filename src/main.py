#from guardSettings import InitGuards

#InitGuards()

#from fileManagement.CSVFile import CSVFile

from m_calendar.calendRa import CalendRa
from fileManagement.buffer import Buffer, BufferCreateI, BufferCreateXY
from ui.console import Console

from calendar import *
"""
def PrintCalendar(calendaR):
    
    for x in range(calendaR.calendar.width):
        print(calendaR.daysHeader.GetI(x).ToText(), end="")
    
    print("\n")
    
    for y in range(calendaR.calendar.height):
        for x in range(calendaR.calendar.width):
            print(calendaR.calendar.GetXY(x, y).ToText(), end="") 
        print("\n")
    
    return
"""
def main():
    
    console = Console() 
       
    console.OnUpdate()
     
    return

main()

