from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY
from datetime import datetime, timedelta

def add_time(start, duration, weekday=None):

    # Checking if weekday argument is given or not. 
    # If so then getting the corresponding date according to weekday. 
    # Format to parse : "1900-01-02 11:43 PM Tuesday"
    # if not, using the default date i.e. 1900-01-01. 
    # Format to parse : "11:06 PM"
    # Finally, parsing string and converting it to datetime object

    if weekday is None:
      start_time = datetime.strptime(start, "%I:%M %p")
    else:
      Week_name = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
      Corresponding_date_for_week = ["1900-01-01", "1900-01-02", "1900-01-03", "1900-01-04", "1900-01-05", "1900-01-06", "1900-01-07"]
      Date_link = Corresponding_date_for_week[Week_name.index(weekday.upper())]
      start = Date_link + " " +start+" "+weekday.capitalize() 
      start_time = datetime.strptime(start, "%Y-%m-%d %I:%M %p %A")
    
    # Getting the hours and minutes into H and M respectively, 
    # creating a time delta variable to use directly with datetime object
    # Finally, addiing delta and start time

    H, M = duration.split(":")
    delta = timedelta(hours=int(H), minutes=int(M))
    new_date_time = start_time + delta
    
    # Checking Weekday to print output in right format

    if weekday is None:
        new_time = datetime.strftime(new_date_time, "%I:%M %p")
    else:
        new_time = datetime.strftime(new_date_time, "%I:%M %p, %A")

    # removing padded 0 if hour start with 0
    if new_time[0] == '0':
        new_time = new_time[1:]

    # Checking new_date_time exceedas start_time by how many days.
    # As such converting into date for substraction
    start_date=start_time.date()
    new_date=new_date_time.date()
    
    # Finally formatting new day to incoporate next days and (n days later) in format
    if new_date - start_date == timedelta(days=1):
        new_time = new_time + " (next day)"
    elif new_date - start_date > timedelta(days=1):
        new_time = new_time + " (" + str((new_date - start_date).days) + " days later)"

    # returning the result
    return new_time