from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    # Set the precision for Decimal calculations
    getcontext().prec = signs_count

    # Calculate the sum of the numbers in the list as Decimals
    total = sum(Decimal(num) for num in number_list)

    # Calculate the average by dividing the total by the number of elements in the list
    average = total / Decimal(len(number_list))

    return average


# Example usage
numbers = [4.5788689699797, 34.7576578697964, 86.8877666656633, 12]
decimal_places = 6
result = decimal_average(numbers, decimal_places)
print(result)  # Output: 34.556
