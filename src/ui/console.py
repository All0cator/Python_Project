from m_calendar.calendRa import CalendRa
from calendar import monthrange

from datetime import date
from datetime import datetime

from m_calendar.event import Event

from ui.menu import Menu, Option, Input

from ui.validationFunctions import *

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

class Console():
    def __init__(self):
        
        self.calendR = CalendRa()
        
        self.PrintEventsForToday()
        
    def PrintEventsForToday(self):
        todayDate = date.today()
        
        year, month, day = str(todayDate).split("-")
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        hour = datetime.now().hour
        minutes = datetime.now().minute
        
        eventsForToday = self.calendR.GetEvents(year, month, day)
        
        if(eventsForToday == None):
            # there are no events :D
            return
        
        for i in range (eventsForToday.size):
            
            e = eventsForToday.GetI(i)
            
            hoursDifference = e.hour - hour
            minsDifference = e.minutes - minutes
            
            # events that are due for today
            print(hoursDifference, minsDifference)
            if(hoursDifference > 0 and minsDifference > 0):
                print("Ειδοποίηση: σε {0} ώρες και {1} λεπτά από τώρα έχει προγραμματιστεί το γεγονός :\n {2}".format(hoursDifference, minsDifference, e.ToText()))
        
    def OnUpdate(self):
        option = ""
        
        while(True):
            if(option == "q"):
                break
            
            self.PrintCalendar()
            print(mainMenu.ToText(), end="")
            
            option = self.GetMenuInput(mainMenu)
            
            if(option == "-"): #left
                
                self.calendR.AdvanceMonth(CalendRa.DIRECTION_PREVIOUS)

            elif(option == ""): #right
                self.calendR.AdvanceMonth(CalendRa.DIRECTION_NEXT)
                
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
                
            elif(option == "*"):
                self.SearchEvents()
                input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:")
    
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
            
        
        alignmentText = "Μη Διαθέσιμα χρονικά κενά: "
        
        print(alignmentText)
        
        for i in range(intervals.size):
            if(intervals.GetI(i).startHourMin != intervals.GetI(i).endHourMin):
                print(len(alignmentText)*" " + intervals.GetI(i).ToText())
        
        newHour = self.ConstructHour(chosenEvent, isBlankF)
        
        newDurationInput = Input("Διάρκεια γεγονότος")
        newDurationValidationFunc = lambda d: DurationValidation(d, isBlankF)
        newDuration = newDurationInput.GetValidatedInput(newDurationValidationFunc)
        
        newTitleInput = Input("Τίτλος γεγονότος")
        newTitleValidationFunc = lambda title: TitleValidation(title, isBlankF)
        newTitle = newTitleInput.GetValidatedInput(newTitleValidationFunc)
        
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
        
        newDate = self.ConstructDate(chosenEvent, lambda x: x == "")
        
        year, month, day = newDate.split("-")
        
        checkDay = self.calendR.GetDayOfYearMonth(int(year), int(month), int(day))
        
        intervals = checkDay.GetDayIntervals()
        if(intervals == None):
            print("Δεν υπάρχουν διαθέσιμα χρονικά κενά για αυτήν την ημερομηνία!")
            return None
        
        alignmentText = "Μη Διαθέσιμα χρονικά κενά: "
        
        print(alignmentText)
        
        for i in range(intervals.size):
            if(intervals.GetI(i).startHourMin != intervals.GetI(i).endHourMin):
                print(len(alignmentText)*" " + intervals.GetI(i).ToText())
        
        newHour = self.ConstructHour(chosenEvent, lambda x: x == "")
        
        newDurationInput = Input("Διάρκεια γεγονότος " + "(" + str(chosenEvent.Get("Duration")) + ")")
        newDurationValidationFunc = lambda d: DurationValidation(d)
        newDuration = newDurationInput.GetValidatedInput(newDurationValidationFunc)
        
        newTitleInput = Input("Τίτλος γεγονότος " + "(" + chosenEvent.Get("Title") + ")")
        newTitleValidationFunc = lambda title: TitleValidation(title)
        newTitle = newTitleInput.GetValidatedInput(newTitleValidationFunc)
        
        if(newDuration == ""):
            newDuration = chosenEvent.Get("Duration")
            
        if(newTitle == ""):
            newTitle = chosenEvent.Get("Title")
        
        chosenEventIndexInCalendR = self.calendR.GetEventIndex(chosenEvent)     
        
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Date", newDate)
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Hour", newHour)
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Duration", newDuration)
        self.calendR.GetEventAt(chosenEventIndexInCalendR).Set("Title", newTitle)  
            
    def SearchEvents(self):
        
        print("=== Αναζήτηση γεγονότων ====")
        
        yearInputField = Input("Εισάγετε έτος")
        yearValidationFunc = lambda y : YearCreateValidation(y)
        year = yearInputField.GetValidatedInput(yearValidationFunc)
        
        monthInputField = Input("Εισάγετε μήνα")
        monthValidationFunc = lambda m: MonthValidation(m, lambda x: False)
        month = monthInputField.GetValidatedInput(monthValidationFunc)
            
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
        
        newYearValidationFunction = lambda y: YearUpdateValidation(y, isBlankF)
        newMonthValidationFunction = lambda m: MonthValidation(m, isBlankF)
        
        print(dateInputText)
        
        
        newYearInput = Input("Χρόνος γεγονότος", " "*len(dateInputText))
        newYear = newYearInput.GetValidatedInput(newYearValidationFunction)
        
        
        newMonthInput = Input("Μήνας γεγονότος", " "*len(dateInputText))
        newMonth = newMonthInput.GetValidatedInput(newMonthValidationFunction)
        
        if(newYear == ""):
            newYear = chosenEvent.year
            
        if(newMonth == ""):
            newMonth = chosenEvent.month
        
        print(newYear, newMonth)
        
        numDaysForNewMonth = monthrange(int(newYear), int(newMonth))[1]
        
        # the validation function needs numDaysForNewMonth to work so we have to define it here and not with the other functions
        newDayValidationFunction = lambda d: DayValidation(d, numDaysForNewMonth, isBlankF)
        
        newDayInput = Input("Ημέρα γεγονότος", " "*len(dateInputText))
        newDay = newDayInput.GetValidatedInput(newDayValidationFunction)
        
        if(newDay == ""):
            newDay = chosenEvent.day
        
        chosenDate = "-".join([str(newYear), str(newMonth), str(newDay)])
        
        return chosenDate
    
    def ConstructHour(self, chosenEvent, isBlankF):
        
        if(chosenEvent == None):
            hourInputText = "Ώρα γεγονότος:"
        else:
            hourInputText = "Ώρα γεγονότος " + "(" + chosenEvent.Get("Hour") + "):"

        newHourValidationFunction = lambda h: HourValidation(h, isBlankF)
        newMinutesValidationFunction = lambda m: MinuteValidation(m, isBlankF)
        
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