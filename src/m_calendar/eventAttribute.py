class EventAttribute:
    def __init__(self, name, val, delimeter=", "):
        self.name = name
        self.val = val
        self.delimeter = delimeter
        
    def ToText(self):
        return self.name + ": " + str(self.val) + self.delimeter