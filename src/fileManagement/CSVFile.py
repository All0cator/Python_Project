from file import *

class CSVFile(File):
    
    def __init__(self, path, isAllowedToWrite=True):
        super().__init__(path, ".csv", True, isAllowedToWrite)
        
        self.ReadFile("r")
        
        fileLines = self.fileContents.strip().split("\n")
        
        
        fileHeaderElements = fileLines[0].split(",")
        
        self.numCols = len(fileHeaderElements)
        self.numRows = len(fileLines)
        
        self.dataTable = Buffer(self.numRows, self.numCols)
        
        for x in range(self.numCols):   
            for y in range(self.numRows):
                self.dataTable.Set(x, y, None)
        
    def ReadFile(self, readMode):
        if(not super().ReadFile(readMode)):
            return False
        
        for x in range(self.dataTable.width):   
            line = self.lineBuffer.Get(x, 1).strip(",")
            for y in range(self.dataTable.height):
                self.dataTable.Set(x, y, line[y])
        
        
    def WriteFile(self, writeMode, content):
        
        #format content into csv format to do
        csvLine = content[0]
        
        return super().WriteFile(writeMode, content)
    
    def GetHeader(self):
        return self.GetRow(1)
    
    def GetNthRecord(self, n):
        return self.GetRow(n)

    def GetRow(self, y):
        
        row = None
        
        for x in range(self.numCols):
            row.append(self.dataTable.Get(x, y))
        
        # rerurns a list ["1st elemnt", "2nd elemtn", ...]
        return row
        
    def GetColumn(self, x):
        
        col = None
        
        for y in range(self.numCols):
            col.append(self.dataTable.Get(x, y))
        
        # remove header from column to be returned
        col.pop()
            
        return col
    
    def GetElementAt(self, x, y):    
        return self.dataTable.Get(x, y)
    
        