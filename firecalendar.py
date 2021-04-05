import calendar

cal = calendar.HTMLCalendar(firstweekday=6)

f = open("calendarweb.html", "w+")
f.write(str(cal.formatmonth(4,3)))
f.close()


