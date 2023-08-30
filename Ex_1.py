from datetime import datetime


def get_days_from_today(date):
    # Splitting the date string into parts using the '-' delimiter
    d = date.split('-')

    # Extracting the year, month, and day from the split parts of the string
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])

    # Creating a datetime object for the provided date
    full_date = datetime(year=year, month=month, day=day)

    # Calculating the difference between the current date and the provided date in days
    result_date = (datetime.now() - full_date).days

    # Returning the result of the difference in days
    return result_date