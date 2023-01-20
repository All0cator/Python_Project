from fileManagement.buffer import Buffer, BufferCreateI, BufferCreateXY

class File:
    """
    ------- Variables -------
    
    <-- path            --> path of file                                (str) ex "\daewdewd\aweda\file.csv"
    <-- extension       --> extension of file                           (str) ex ".csv"
    <-- isAllowedToRead --> flag that permits read activities on file:  (bool)
                            True  if is allowed to read file
                            False if not allowed to read file 
    <-- isAllowedToWrite--> flag that permits write activities on file: (bool)
                            True  if is allowed to write to file
                            False if not allowed to write to file  
    <-- fileContents    --> Object that stores each line of file        (Buffer) ex it is a one dimensional buffer that each element is a line of the file
                            (a line is always terminated by character \n)
    """
    
    writeModes = {"w", "a"}
    readModes = {"r"}
    readWriteModes = {"w+", "a+", "r+"}
    
    def __init__(self, path, extension, isAllowedToRead=True, isAllowedToWrite=True):
        self.path = path
        self.extension = extension
        self.isAllowedToRead = isAllowedToRead
        self.isAllowedToWrite = isAllowedToWrite
        
        
    def ReadFile(self, readMode):
        if(not self.isAllowedToRead):
            print("Error: Not allowed to read file at: " + self.path + " because file cannot be opened for reading.")
            return False
        
        if((not readMode in File.readModes) and (not readMode in File.readWriteModes)):
            print("Error: Function ReadFile got wrong readMode: " + readMode + " is not a valid readMode")
            return False
        
        file = open(self.path, readMode)
        
        fileLines = file.readlines()
        
        if(fileLines == False):
            self.fileContents == None
            return
        
        self.fileContents = BufferCreateI(len(fileLines))

        for x in range(len(fileLines)):
            self.fileContents.SetI(x, fileLines[x])
        
        file.close()
        
        return True
        

    def WriteFile(self, writeMode, contentBuffer):
        if(not self.isAllowedToWrite):
            print("Error: Not allowed to write file at: " + self.path + " because file cannot be opened for writing.")
            return False
        
        if((not writeMode in File.writeModes) and (not writeMode in File.readWriteModes)):
            print("Error: Function WriteFile got wrong writeMode: " + writeMode + " is not a valid writeMode")
            return False
        
        file = open(self.path, writeMode)      
        
        file.write(self.BufferToText(contentBuffer))
        
        self.fileContents = contentBuffer
        
        file.close()
        
        return True
    
    def BufferToText(self, buffer):
        
        text = ""
        
        if(self.extension == ".csv"):
            text += "Date,Hour,Duration,Title\n"
        
        for y in range(buffer.height):
            for x in range(buffer.width):
                if(buffer.GetXY(x, y) != None):
                    text += buffer.GetXY(x, y)
        
            # if the final character of text is not a newline then add a new line to it
            if(text[len(text) - 1] != "\n"):
                text += "\n"
            
        return text
