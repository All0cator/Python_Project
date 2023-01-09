#UI : User Interface
# These are all the "printable" elements on the screen

from m_calendar.separator import Separator

#class UIElement:
#    def __init__(self, textPlaceholder=""):
#        self.text = textPlaceholder

class Menu():
    def __init__(self, header, options, input_, textLineTop=""):
        #super().__init__(header)
        self.header = header
        self.options = options
        self.input = input_
        self.lineTop = Line(textLineTop)
        
    def ToText(self):
        
        string = ""
        
        # add line separator at top
        
        #if there is an empty line there is no point to append it
        if(len(self.lineTop.ToText()) > 0):
            string += self.lineTop.ToText() + "\n"
        
        # add header to text
        
        string += self.header + "\n"
        
        # add each option to text
        
        for option in self.options:
            string += "    " + option.ToText() + "\n"
        
        return string
    
    
    def GetInputText(self):
        return "    " + self.input.ToText()
        

class Option():
    def __init__(self, text, textLeftSeparator="", textRightSeparator=""):
        self.text = text
        self.separatorLeft = Separator(textLeftSeparator)
        self.separatorRight = Separator(textRightSeparator)
        
    def ToText(self):
        return self.separatorLeft.ToText() + self.text + self.separatorRight.ToText()

class Input():
    def __init__(self, text, textLeftSeparator="", textRightSeparator=""):
        #super().__init__(text)
        self.text = text
        self.separatorLeft = Separator(textLeftSeparator)
        self.separatorRight = Separator(textRightSeparator)
    
    def ToText(self):
        return self.separatorLeft.ToText() + self.text + self.separatorRight.ToText()

class Line(Separator):
    def __init__(self, text):
        super().__init__(text, True)