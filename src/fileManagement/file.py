from buffer import Buffer

class File:
    
    # Variables in class:
    # path
    # extension
    # isAllowedToRead
    # isAllowedToWrite
    # fileContents
    
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
        
        if((not readMode in self.readModes) or (not readMode in self.readWriteModes)):
            print("Error: Function ReadFile got wrong readMode: " + readMode + " is not a valid readMode")
            return False
        
        file = open(self.path, readMode)
        
        fileLines = file.readlines()
        
        self.lineBuffer = Buffer(len(fileLines), 1)

        for x in range(len(fileLines)):
            self.lineBuffer.Set(x, 1, fileLines[x])
        
        file.close()
        
        return True
        

    def WriteFile(self, writeMode, content):
        if(not self.isAllowedToWrite):
            print("Error: Not allowed to write file at: " + self.path + " because file cannot be opened for writing.")
            return False
        
        if((not writeMode in self.writeModes) or (not writeMode in self.readWriteModes)):
            print("Error: Function WriteFile got wrong writeMode: " + writeMode + " is not a valid writeMode")
            return False
        
        file = open(self.path, writeMode)
        
        file.write(content)
        
        self.fileContents = None
        
        file.close()
        
        return True
    
    # Note this will not be part of the file.py final version its just for debuggin purposes
    
    def PrintFileContents(self):
        for i in range(self.fileContents.size):
            print(self.fileContents.Get(i, 1))
