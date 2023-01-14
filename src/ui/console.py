from ui.surface import Surface
from m_calendar.calendRa import CalendRa

from ui.menu import Menu, Option, Input

CONSOLE_LINE_LENGTH = 50


mainMenuHeader = "Πατήστε ENTER για προβολή του επόμενου μήνα, \"q\" για έξοδο ή κάποια από τις παρακάτω επιλογές:"
mainMenuOptions = [ Option("για πλοήγηση στον προηγούμενο μήνα", "\"-\" "),          
                    Option("για διαχείριση των γεγονότων του ημερολογίου", "\"+\" "),     
                    Option("για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα", "\"*\" ")]
mainMenuInput = Input("->")
mainMenuAvailableOptions = ["q", "-", "+", "*", ""]

mainMenu = Menu(mainMenuHeader, mainMenuOptions, mainMenuInput, mainMenuAvailableOptions, "-")

#menu = """Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις
#        παρακάτω επιλογές:
#        "-" για πλοήγηση στον προηγούμενο μήνα
#        "+" για διαχείριση των γεγονότων του ημερολογίου
#        "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα
 #       ->"""

manageMenuHeader = "Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:"
manageMenuOptions = [ Option("Καταγραφή νέου γεγονότος", "1 "),
                      Option("Διαγραφή γεγονότος", "2 "),
                      Option("Ενημέρωση γεγονότος", "3 "),
                      Option("Επιστροφή στο κυρίως μενού", "0 ")]
manageMenuInput = Input("->")

manageMenuAvailableOptions = ["1", "2", "3", "0"]

manageMenu = Menu(manageMenuHeader, manageMenuOptions, manageMenuInput, manageMenuAvailableOptions, "-")

class Console(Surface):
    def __init__(self):
        
        self.calendR = CalendRa()
        
    def OnUpdate(self):
        
        self.PrintCalendar()
        print(mainMenu.ToText(), end="")
        
        option = input()
        
        while(True):
            if(option == "q"):
                break
            
            if(option == "-"): #left
                self.calendR.AdvanceMonth(CalendRa.DIRECTION_PREVIOUS)
                
                self.PrintCalendar()
                print(mainMenu.ToText(), end="")
                
                option = self.GetMenuInput(mainMenu)
                
                continue

            elif(option == ""): #right
                self.calendR.AdvanceMonth(CalendRa.DIRECTION_NEXT)
                
                self.PrintCalendar()
                print(mainMenu.ToText(), end="")
                
                option = self.GetMenuInput(mainMenu)
                
                continue
            elif(option == "+"):
                print(manageMenu.ToText(), end="")
                
                option = self.GetMenuInput(manageMenu)
                
                if(option == "1"):
                    self.SearchEvents()
                elif(option == "2"):
                    self.SearchEvents()
                elif(option == "3"):
                    self.SearchEvents()
                elif(option == "0"):
                    pass
                continue
                
            elif(option == "*"):
                pass
                
            option = input()
        
            
    def SearchEvents(self):
        
            
    def GetMenuInput(menu):
        option = input(menu.GetInputText())
                
        while(option not in menu.availableOptions):
            option = input(menu.GetInputText())
            
        return option
    
    def PrintCalendar(self):
        
        print("_"*CONSOLE_LINE_LENGTH + "\n")
        print(CalendRa.months[self.calendR.currentMonth.value - 1] + "  " + str(self.calendR.currentMonth.year))
        print("_"*CONSOLE_LINE_LENGTH + "\n")
        
        for x in range(self.calendR.calendar.width):
            print(self.calendR.daysHeader.GetI(x).ToText(), end="")
        
        print("\n")
        
        for y in range(self.calendR.calendar.height):
            for x in range(self.calendR.calendar.width):
                print(self.calendR.calendar.GetXY(x, y).ToText(), end="") 
            print("\n")
    
    #def PrintMenu(self, header, options, isNumbered=False):
    #    optionsLeftSeparators = 
    #    if(isNumbered):
    #        for i in range optionsLeftSeparators