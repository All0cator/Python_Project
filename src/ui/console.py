from ui.surface import Surface
from m_calendar.calendRa import CalendRa
from calendar import monthrange

from datetime import date
from datetime import datetime

from m_calendar.event import Event

from ui.menu import Menu, Option, Input

CONSOLE_LINE_LENGTH = 50


mainMenuHeader = "Πατήστε ENTER για προβολή του επόμενου μήνα, \"q\" για έξοδο ή κάποια από τις παρακάτω επιλογές:"
mainMenuOptions = [ Option("για πλοήγηση στον προηγούμενο μήνα", "\"-\" "),          
                    Option("για διαχείριση των γεγονότων του ημερολογίου", "\"+\" "),     
                    Option("για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα", "\"*\" ")]
mainMenuInput = Input("->")
mainMenuAvailableOptions = ["q", "-", "+", "*", ""]

mainMenu = Menu(mainMenuHeader, mainMenuOptions, mainMenuInput, mainMenuAvailableOptions, "-")


manageMenuHeader = "Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:"
manageMenuOptions = [ Option("Καταγραφή νέου γεγονότος", "1 "),
                      Option("Διαγραφή γεγονότος", "2 "),
                      Option("Ενημέρωση γεγονότος", "3 "),
                      Option("Επιστροφή στο κυρίως μενού", "0 ")]
manageMenuInput = Input("->")

manageMenuAvailableOptions = ["1", "2", "3", "0"]

manageMenu = Menu(manageMenuHeader, manageMenuOptions, manageMenuInput, manageMenuAvailableOptions, "")

class Console(Surface):
    def __init__(self):
        
        self.calendR = CalendRa()
        
        self.PrintEventsForToday()
        
    def PrintEventsForToday(self):
        todayDate = date.today()
        
        year, month, day = str(todayDate).split("-")
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        
        # dont ask about + 2 the docs about datetime are so bad i have to offset the hour i get by 2 hours
        # thats some timezone problem in which cannot be solved without external libraries
        
        hour = datetime.now().hour + 2 # magic
        
        eventsForToday = self.calendR.GetEvents(year, month, day)
        
        if(eventsForToday == None):
            # there are no events :D
            return
        
        for i in range (eventsForToday.size):
            
            e = eventsForToday.GetI(i)
            
            hourDifference = e.hour - hour
            
            # events that are due for today
            if(hourDifference > 0):
                print("Ειδοποίηση: σε {0} ώρες από τώρα έχει προγραμματιστεί το γεγονός :\n {1}".format(hourDifference, e.ToText()))
        
    def OnUpdate(self):
        
        #self.PrintCalendar()
        #print(mainMenu.ToText(), end="")
        
        #option = input()
        
        option = ""
        
        firstRun = True
        
        while(True):
            if(option == "q"):
                break
            
            self.PrintCalendar()
            print(mainMenu.ToText(), end="")
            
            #if(firstRun):
            option = self.GetMenuInput(mainMenu)
            
            if(option == "-"): #left
                
                self.calendR.AdvanceMonth(CalendRa.DIRECTION_PREVIOUS)
                
                #option = self.GetMenuInput(mainMenu)
                
                # we use continue because we just got an option up here
                # then below we would get another option that would overwrite our option up here
                # This is used to simulate the different menu levels
                # mainMenu
                #       manageMenu
                
                #continue

            elif(option == ""): #right
                self.calendR.AdvanceMonth(CalendRa.DIRECTION_NEXT)
                
                #self.PrintCalendar()
                #print(mainMenu.ToText(), end="")
                
                #option = self.GetMenuInput(mainMenu)
                
                #continue
            elif(option == "+"):
                print(manageMenu.ToText(), end="")
                
                option = self.GetMenuInput(manageMenu)
                
                if(option == "1"):
                    self.CreateEvent()
                    self.calendR.SaveEvents("assets\\csvFiles\\events.csv")
                elif(option == "2"):
                    self.DeleteEvent()
                    self.calendR.SaveEvents("assets\\csvFiles\\events.csv")
                elif(option == "3"):
                    self.UpdateEvent()
                    self.calendR.SaveEvents("assets\\csvFiles\\events.csv")
                elif(option == "0"):
                    pass
                #continue
                
            elif(option == "*"):
                self.SearchEvents()
                input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:")
            
            #option = input()
    
    def CreateEvent(self):
        
        #Python doesnt have a do while loop so we have to do it this way :D
        
        newEvent = self.NewEventFromInput(None)
        
        while(newEvent == None or newEvent.OverlapsWithOtherEvents(self.calendR.events)):
            print("Το γεγονός επικαλύπτεται απο άλλο γεγονός ξαναδώστε στοιχεία.")
            
            newEvent = self.NewEventFromInput(None)
        
        self.calendR.AddEvent(newEvent)
    
    def NewEventFromInput(self, chosenEvent):
        
        # if i dont give any event so chosenEvent == None
        # then that means that i want to create an event in which case i dont want
        # any validation function to get blank "" inputs
        if(chosenEvent == None):
            isBlankF = lambda x: False
        else:
            isBlankF = lambda x : x == ""
        
        newDate = self.ConstructDate(chosenEvent, isBlankF)
        
        year, month, day = newDate.split("-")
        
        checkDay = self.calendR.GetDayOfYearMonth(int(year), int(month), int(day))
        
        intervals = checkDay.GetDayIntervals()
        if(intervals == None):
            print("Δεν υπάρχουν διαθέσιμα χρονικά κενά για αυτήν την ημερομηνία!")
            return None
            
        
        alignmentText = "Διαθέσιμα χρονικά κενά: "
        
        print(alignmentText)
        
        for i in range(intervals.size):
            #if(intervals.GetI(i).startHourMin != intervals.GetI(i).endHourMin):
            print(len(alignmentText)*" " + intervals.GetI(i).ToText())
        
        newHour = self.ConstructHour(chosenEvent, isBlankF)
        
        newDurationInput = Input("Διάρκεια γεγονότος")
        newDuration = newDurationInput.GetValidatedInput(lambda dur: dur > 0 or isBlankF(dur))
        
        newTitleInput = Input("Τίτλος γεγονότος")
        newTitle = newTitleInput.GetValidatedInput(lambda title : (not type(title) == int and not "," in str(title)) or isBlankF(title))
        
        eventAttributes = [newDate, newHour, str(newDuration), newTitle]
        
        newEvent = Event(eventAttributes)
        
        return newEvent
    
    def DeleteEvent(self):
        selectedEvents = self.SearchEvents()
        
        if(selectedEvents == None):
            return
        
        eventChoiceInputField = Input("Επιλέξτε γεγονός προς διαγραφή")
        eventChoice = eventChoiceInputField.GetValidatedInput(lambda choice: choice < selectedEvents.size)

        chosenEvent = selectedEvents.GetI(eventChoice)
        
        self.calendR.DelEvent(chosenEvent)
        
    def UpdateEvent(self):
        selectedEvents = self.SearchEvents()
        
        if(selectedEvents == None):
            return
        
        eventChoiceInputField = Input("Επιλέξτε γεγονός προς ενημέρωση")
        eventChoice = eventChoiceInputField.GetValidatedInput(lambda choice: choice < selectedEvents.size)
        
        chosenEvent = selectedEvents.GetI(eventChoice)
        
        newDate = self.ConstructDate(chosenEvent, lambda x: False)
        
        year, month, day = newDate.split("-")
        
        checkDay = self.calendR.GetDayOfYearMonth(year, month, day)
        
        intervals = checkDay.GetDayIntervals()
        
        alignmentText = "Διαθέσιμα χρονικά κενά: "
        
        print(alignmentText)
        
        for i in range(intervals.size):
            print(len(alignmentText)*" " + intervals.GetI(i))
        
        newHour = self.ConstructHour(chosenEvent, lambda x: False)
        
        newDurationInput = Input("Διάρκεια γεγονότος " + "(" + str(chosenEvent.Get("Duration")) + ")")
        newDuration = newDurationInput.GetValidatedInput(lambda dur: dur > 0 or dur == "")
        
        newTitleInput = Input("Τίτλος γεγονότος " + "(" + chosenEvent.Get("Title") + ")")
        newTitle = newTitleInput.GetValidatedInput(lambda title : (not type(title) == int and not "," in str(title)) or str(title) == "")
        
        
        if(newDuration == ""):
            newDuration = chosenEvent.Get("Duration")
            
        if(newTitle == ""):
            newTitle = chosenEvent.Get("Title")
        
        chosenEventIndexInCalendR = self.calendR.GetEventIndex(chosenEvent)
        
        
        
        newEvent = Event([newDate, newHour, str(newDuration), newTitle])
        
        
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Date", newDate)
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Hour", newHour)
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Duration", str(newDuration))
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Title", newTitle)  
            
    def SearchEvents(self):
        
        print("=== Αναζήτηση γεγονότων ====")
        
        yearInputField = Input("Εισάγετε έτος")
        year = yearInputField.GetValidatedInput(lambda y: y >= 1 and y <= 9999)
        
        monthInputField = Input("Εισάγετε μήνα")
        month = monthInputField.GetValidatedInput(lambda m: m >= 1 and m <= 12)
        
        tup = self.calendR.GetEventsText(year, month)
        
        eventsText = tup[0]
        selectedEvents = tup[1]
        
        print(eventsText)
        
        return selectedEvents
    
    def ConstructDate(self, chosenEvent, isBlankF):
        
        if(chosenEvent == None):
            dateInputText = "Ημερομηνία γεγονότος:"
        else:
            dateInputText = "Ημερομηνία γεγονότος " + "(" + chosenEvent.Get("Date") + "):"
        
        newYearValidationFunction = lambda year: year >= 2022 or isBlankF(year)
        newMonthValidationFunction = lambda m: (m >= 1 and m <= 12) or isBlankF(m)
        
        print(dateInputText)
        
        
        newYearInput = Input("Χρόνος γεγονότος", " "*len(dateInputText))
        newYear = newYearInput.GetValidatedInput(newYearValidationFunction)
        
        
        newMonthInput = Input("Μήνας γεγονότος", " "*len(dateInputText))
        newMonth = newMonthInput.GetValidatedInput(newMonthValidationFunction)
        
        numDaysForNewMonth = monthrange(newYear, newMonth)[1]
        
        # the validation function needs numDaysForNewMonth to work so we have to define it here and not with the other functions
        newDayValidationFunction = lambda d: (d >= 1 and d <= numDaysForNewMonth) or isBlankF(d)
        
        newDayInput = Input("Ημέρα γεγονότος", " "*len(dateInputText))
        newDay = newDayInput.GetValidatedInput(newDayValidationFunction)
        
        if(newYear == ""):
            newYear = chosenEvent.year
            
        if(newMonth == ""):
            newMonth = chosenEvent.month
        
        if(newDay == ""):
            newDay = chosenEvent.day
        
        chosenDate = "-".join([str(newYear), str(newMonth), str(newDay)])
        
        return chosenDate
    
    def ConstructHour(self, chosenEvent, isBlankF):
        
        if(chosenEvent == None):
            hourInputText = "Ώρα γεγονότος:"
        else:
            hourInputText = "Ώρα γεγονότος " + "(" + chosenEvent.Get("Hour") + "):"

        newHourValidationFunction = lambda h: (h >= 0 and h <= 23) or isBlankF(h)
        newMinutesValidationFunction = lambda m: (m >= 0 and m <= 59) or isBlankF(m)
        
        print(hourInputText)
        
        newHourInput = Input("Ώρες γεγονότος", " "*len(hourInputText))
        newHour = newHourInput.GetValidatedInput(newHourValidationFunction)
        
        
        newMinutesInput = Input("Λεπτά γεγονότος", " "*len(hourInputText))
        newMinutes = newMinutesInput.GetValidatedInput(newMinutesValidationFunction)
        
        if(newHour == ""):
            newHour = chosenEvent.hour
            
        if(newMinutes == ""):
            newMinutes = chosenEvent.minutes
            
        chosenHour = ":".join([str(newHour), str(newMinutes)])
        
        return chosenHour

    def GetMenuInput(self, menu):
        option = input(menu.GetInputText())
                
        while(option not in menu.availableOptions):
            option = input(menu.GetInputText())
            
        return option
    
    def PrintCalendar(self):
        
        print("_"*CONSOLE_LINE_LENGTH + "\n")
        print(CalendRa.months[self.calendR.currentYear.currentMonth.value - 1] + "  " + str(self.calendR.currentYear.value))
        print("_"*CONSOLE_LINE_LENGTH + "\n")
        
        for x in range(self.calendR.calendar.width):
            print(self.calendR.daysHeader.GetI(x).ToText(), end="")
        
        print("\n")
        
        for y in range(self.calendR.calendar.height):
            for x in range(self.calendR.calendar.width):
                print(self.calendR.calendar.GetXY(x, y).ToText(), end="") 
            print("\n")