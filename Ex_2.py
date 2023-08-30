from datetime import date


def get_days_in_month(month, year):
    # Check if the input month is valid (between 1 and 12) and if the year is a 4-digit number
    if 1 <= month <= 12 and len(str(year)) == 4:
        # Create a date object for the first day of the specified month and year
        d1 = date(year=year, month=month, day=1)

        # Calculate the year of the next month and adjust if it's a new year
        future_year = d1.year + (d1.month // 12)

        # Calculate the month of the next month (adjusting if it's a new year)
        future_month = (d1.month % 12) + 1

        # Create a date object for the first day of the next month
        future_date = date(year=future_year, month=future_month, day=1)

        # Calculate the number of days between the first day of the next month and the first day of the current month
        day_in_month = (future_date - d1).days

        return day_in_month
    else:
        return 0  # Invalid input

# Example usage
print(get_days_in_month(2, 2023))  # Output: 28