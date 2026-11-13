import datetime
event = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
eventDate = datetime.date(year, month, day)

print(f"Event: {event.upper()}")
print(f"Date: {eventDate.strftime("%B %-d, %Y")}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday: {eventDate.strftime("%A")}")
