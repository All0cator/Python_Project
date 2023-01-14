#from ui.console import CONSOLE_LINE_LENGTH


CONSOLE_LINE_LENGTH = 50

class Separator:
    def __init__(self, text="", isALine=False):
        self.text = text
        self.isALine = isALine
        
    def ToText(self):
        
        if(len(self.text) == 0):
            return self.text
        
        if(not self.isALine):
            return self.text
        
        if(len(self.text) > CONSOLE_LINE_LENGTH):
            return self.text


        line = self.text
        while(len(line) < CONSOLE_LINE_LENGTH):
            for char in self.text:
                line += char
                
        return line
    
    def Append(self, value):
        if(self.isALine):
            assert(False and "Error: Cannot append more text in a line.")
        
        self.text += value

    def ReplaceEndCharacterWith(self, value):
        if(self.isALine):
            assert(False and "Error: Replacing text in a line is not allowed.")

        self.text = self.text[:len(self.text) - 1] + value