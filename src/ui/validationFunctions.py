def YearCreateValidation(y):
    return y >= 1 and y <= 9999
        
def YearUpdateValidation(y, isBlankF=lambda x: x == ""):
    
    try:
        if(int(y) >= 2022 or isBlankF(y)):
            return True
    except ValueError:
        
        return isBlankF(y)
        
    return False
def MonthValidation(m, isBlankF=lambda x: x == ""):
    try:
        if((int(m) >= 1 and int(m) <= 12) or isBlankF(m)):
            return True
    except ValueError:
        
        return isBlankF(m)
        
    return False

def DayValidation(d, numDaysForNewMonth, isBlankF=lambda x: x == ""):
    try:
        if((int(d) >= 1 and int(d) <= numDaysForNewMonth) or isBlankF(d)):
            return True
    except ValueError:
        
        return isBlankF(d)
        
    return False

def HourValidation(h, isBlankF=lambda x: x == ""):
    try:
        if((int(h) >= 0 and int(h) <= 23) or isBlankF(h)):
            return True
    except ValueError:
        
        return isBlankF(h)
        
    return False

def MinuteValidation(m, isBlankF=lambda x: x == ""):
    try:
        if((int(m) >= 0 and int(m) <= 59) or isBlankF(m)):
            return True
    except ValueError:
        
        return isBlankF(m)
        
    return False

def DurationValidation(d, isBlankF=lambda x: x == ""):
    
    try:
        if(int(d) > 0 or isBlankF(d)):
            return True
    except ValueError:
        
        return isBlankF(d)
        
    return False

def TitleValidation(title, isBlankF=lambda x: x == ""):
    
    try:
        if((type(title) == str and not "," in str(title)) or isBlankF(title)):
            return True
    except ValueError:
        
        return False
        
    return False