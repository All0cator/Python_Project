#from guardSettings import InitGuards

#InitGuards()

from fileManagement.CSVFile import CSVFile

def main():
    
    file = CSVFile("assets/csvFiles/covid19.csv", False)
    
    file.ReadFile("r")
    
    print(file.dataTable.data)
    
    return

main()