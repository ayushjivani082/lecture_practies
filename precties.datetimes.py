from datetime import datetime , timedelta , timezone

import time

# Current Date and Time

def current_datetime():
    now = datetime.now()
    print("Current Date and Time:", now)

    print("Year:" , now.year)

    print("Month:" , now.month)

    print("Day:" , now.day)

    print("Hour:" , now.hour)

    print("Minute:" , now.minute)

    print("second:" , now.second)

current_datetime()

# current time in seconds

def time_second():

    second = time.time()

    print("\n Time in Seconds")

    print(second)

time_second()

# Date and time formatting

def format_datetime():
    now = datetime.now()

    print("\n Date and Time Formatting")

    print("DD-MM-YYYY : " , now.strftime("%d-%m-%Y"))
    print("DD-MM-YYYY : " , now.strftime("%d/%m/%y"))
    print("DD-MM-YYYY : " , now.strftime("%m/%d/%Y"))
    print("DD-MM-YYYY : " , now.strftime("%m/%d/%y"))
    print("DD-MM-YYYY : " , now.strftime("%I %M, %S"))
    print("DD-MM-YYYY : " , now.strftime("%H:%M:%S"))

    format_datetime()

# Number of days between two dates
def date_difference():

    start_date = input("Enter start date(YYYY-MM-DD):")
    end_date = input("Enter end date(YYYY-MM-DD):")


    date1 = datetime.strptime(start_date , "%Y-%m-%d")
    date2 = datetime.strptime(end_date , "%Y-%m-%d")

    days = abs((date2 - date1).days)

    print("Total Days :" , days)

date_difference()