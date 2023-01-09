from datetime import *

class Event:
    def __init__(self, year, month, day, hour, duration, title):
        self.date = datetime.date(year, month, day)
        self.hour = hour
        self.duration = duration
        self.title = title
    