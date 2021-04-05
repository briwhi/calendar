import calendar
import datetime

class WorkCalendar:
    def __init__(self, 
    year=datetime.datetime.now().year,
    month=datetime.datetime.now().month):
        self.year = year
        self.month = month

        
c = WorkCalendar(month=6)
print(c.month)


