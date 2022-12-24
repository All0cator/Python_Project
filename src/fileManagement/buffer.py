
class Buffer:
    """
    -+-+-+- Buffer Class -+-+-+-
    
    ------- Brief -------
    
    This class is used as an abstraction to the calculation of index of a 1 dimensional
    list to a 2 dimensional list
    The calculation is the following:
    if we have 2 lists with the same elements dimension1List[number of columns * number of rows] and dimension2List[number of rows][number of columns]
    then
    dimension1List[index y * width + x] == dimension2List[y][x], for every x, y that x < number of columns, y < number of rows
    
    ------- Creation -------
    
    To create an object of type Buffer all you have to do is:
    new_buffer = Buffer(numRows, numCols)
    
    ------- Functions -------
    
    To access data at (x, y) we use 2 functions:
    
    ------- Get(x, y): returns data stored in yth row and xth column
                       if x and y are out of bounds it prints "Error: Buffer out of index coords (x, y)"
    ------- Set(x, y): sets the data stored in yth row and xth column
                       if x and y are out of bounds it prints "Error: Buffer out of index coords (x, y)"
    """
    def __init__(self, numRows, numCols):
        
        self.width = numCols
        self.height = numRows
        
        self.size = numCols * numRows
        
        for i in range(self.size):
            self.data.append(None)
        
    def Get(self, x, y):
        if(y >= self.height and x >= self.width):
            print("Error: Buffer out of index coords (" + str(x) +", " + str(y) +")")
            return
        
        return str(self.data[y * self.width + x])
    
    def Set(self, x, y, value):
        if(y >= self.height and x >= self.width):
            print("Error: Buffer out of index coords (" + str(x) +", " + str(y) +")")
            return
        
        self.data[y * self.width + x] = value
        