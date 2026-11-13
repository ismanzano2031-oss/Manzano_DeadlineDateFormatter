from datetime import date
from datetime import datetime
event = input("Enter event title: ")
year = input("Enter year: ")
month = input("Enter month: ")
day = input("Enter day: ")
eventDate = datetime.date(year, month, day)

print(f"Event: {event.upper()}")
print(f"Date: {eventDate.strftime("%B, %-d, %Y")}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday: {date.strftime("%A")}")
