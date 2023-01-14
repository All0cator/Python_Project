class EventAttribute:
    def __init__(self, val, delimeter=", "):
        self.val = val
        self.delimeter = delimeter
        
    def ToText(self):
        return self.name + ": " + self.val + self.delimeter