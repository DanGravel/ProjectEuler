import datetime

"""
Counts the number of sundays that fall on the first of the month from 1901 to 2000
Result: 171
Runtime:0.0005013942718505859
"""
def problem19():
    sundays = 0
    for year in range(1901,2001):
        for month in range(1, 13):
            if(datetime.date(year,month,1).weekday() == 6):
                sundays += 1
    return sundays
           
