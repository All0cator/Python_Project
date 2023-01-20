from fileManagement.file import *

class CSVFile(File):
    """
    ------- Variables -------
    
    all variables of (File) object + 
    <-- numRows   --> number of rows of dataTable                          (int)
    <-- numCols   --> number of columns of dataTable                       (int)
    <-- dataTable --> an object that stores data of a csv file separated : (Buffer) ex It is a 2 dimensional buffer because we want rows and collumns 
    into rows and collumns of data as it is organized in the file
    
    """
    
    def __init__(self, path, isAllowedToWrite=True):
        
        super().__init__(path, ".csv", True, isAllowedToWrite)
                
        if(not self.ReadFile("r")):
            assert(False and "Lol cannot read file")
        
    def ReadFile(self, readMode):
        if(not super().ReadFile(readMode)):
            assert(False and "Failed to read file lol")
        
        fileHeaderElements = self.fileContents.GetI(0).split(",")
        
        self.numCols = len(fileHeaderElements)
        self.numRows = self.fileContents.size
        
        self.dataTable = BufferCreateXY(self.numCols, self.numRows)
                
        for y in range(self.dataTable.height): 
            
            # always make sure csv file ends with an \n (endline character) or else 
            # csv file data extraction misses final data member of file becasue below we are cutting last character of every line
            # which is \n so always insert a \n at the end of the csv file 
              
            line = (self.fileContents.GetI(y))[:-1].split(",")
            
            for x in range(self.dataTable.width):
                self.dataTable.SetXY(x, y, line[x])
        
        return True
        
    def WriteFile(self, writeMode, contentBuffer):
        
        if(contentBuffer == None):
            return
    
        return super().WriteFile(writeMode, contentBuffer)
    def GetHeader(self):
        return self.GetRow(0)
    
    def GetNthRecord(self, n):
        return self.GetRow(n)
    
    def GetFinalRecord(self):
        return self.GetRow(self.numRows - 1)

    def GetRow(self, y):
        
        row = list()
        
        for x in range(self.numCols):
            row.append(self.dataTable.GetXY(x, y))
        
        # rerurns a list ["1st elemnt", "2nd elemtn", ...]
        return row
    
    def GetColumn(self, x):
        
        col = list()
        
        for y in range(self.numRows):
            col.append(self.dataTable.GetXY(x, y))
        
        # remove header from column to be returned
        
        col.pop(0)
            
        return col
    
    def GetElementAt(self, x, y):    
        return self.dataTable.GetXY(x, y)
    
        