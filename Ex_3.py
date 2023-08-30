from datetime import datetime


def get_str_date(date):
    # Printing the input date for debugging purposes
    print(date)

    # Splitting the input date into parts using ' ' as the delimiter
    d_ = date.split(' ')

    # Splitting the first part of the input date (containing year-month-day) into separate components
    d = d_[0].split('-')
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])

    # Creating a datetime object for the specified year, month, and day
    full_date = datetime(year=year, month=month, day=day)

    # Formatting the datetime object into a string with the desired format: 'DayOfMonth Month Year'
    formatted_date = full_date.strftime('%A %d %B %Y')

    return formatted_date


# Example usage
input_date = '2021-05-27 17:08:34.149Z'
result = get_str_date(input_date)
print(result)  # Output: 'Thursday 27 May 2021'