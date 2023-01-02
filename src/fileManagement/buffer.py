#from guardSettings import BUFFER_INCLUDED_GUARD

#if not BUFFER_INCLUDED_GUARD:
#    BUFFER_INCLUDED_GUARD = True
    
    # import statements for file buffer.py


# h python den uposthrizei constructor overload opote kano auth thn patenta gia thn dhmiourgia buffer
# syntactic sugar for Object creation

# one dimensional buffer
def BufferCreateI(i):
    return Buffer(i, 1)

# two dimensional buffer
    
def BufferCreateXY(numCols, numRows):
    return Buffer(numCols, numRows)

# no reason to create higher dimension buffers :D

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
    new_buffer = BufferCreateXY(numCols, numRows)
    
    ------- Functions -------
    
    To access data at (x, y) we use 2 functions:
    
    ------- GetXY(x, y): returns data stored in yth row and xth column
                       if x and y are out of bounds it prints "Error: Buffer out of index coords (x, y)"
    ------- SetXY(x, y): sets the data stored in yth row and xth column
                       if x and y are out of bounds it prints "Error: Buffer out of index coords (x, y)"
    """
    """ 
    ------- Variables -------

    <-- width  --> number of columns of buffer                          (int)
    <-- height --> number of rows of buffer                             (int)
    <-- size   --> total number of cells of buffer                      (int)
    <-- data   --> the data table which holds information in each cell  (list)
    
    """
    
    def __init__(self, numCols, numRows):
        
        if(numRows <= 0 or numCols <= 0):
            print("Error: Non-positive dimensions given to buffer: (Width=" + str(numCols) + ", Height=" + str(numRows) + ")")
            return
        
        self.width = numCols
        self.height = numRows
        
        self.size = numCols * numRows
        
        self.data = list()
        
        for i in range(self.size):
            self.data.append(None)
    
    # treat buffer as 2 dimensional array
        
    def GetXY(self, x, y):
        if(y >= self.height or x >= self.width):
            print("Error: Buffer out of index coords (" + str(x) +", " + str(y) +")")
            return
        
        return str(self.data[y * self.width + x])
    
    # treat buffer as 1 dimensional array

    def GetI(self, index):
        
        x = index % self.width
        y = index // self.width
        
        return self.GetXY(x, y)
    
    # treat buffer as 2 dimensional array
    
    def SetXY(self, x, y, value):
        if(y >= self.height or x >= self.width):
            print("Error: Buffer out of index coords (" + str(x) +", " + str(y) +")")
            return

        self.data[y * self.width + x] = value
    
    # treat buffer as 1 dimensional array
    
    def SetI(self, index, value):
                
        x = index % self.width
        y = index // self.width
        
        self.SetXY(x, y, value)