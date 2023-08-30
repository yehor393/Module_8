from random import randrange


def get_numbers_ticket(min_val, max_val, quantity):
    # Create an empty set to store unique numbers
    num_set = set()

    # Check if the provided input values are valid
    if min_val >= 1 and max_val <= 1000 and min_val < quantity < max_val:
        # Generate random numbers and add them to the set until the desired quantity is reached
        while len(num_set) < quantity:
            number = randrange(min_val, max_val)
            num_set.add(number)
    else:
        return []  # Invalid input, return an empty list

    # Convert the set of numbers to a sorted list and return it
    return sorted(list(num_set))


# Example usage
min_value = 1
max_value = 1000
quantity = 6
result = get_numbers_ticket(min_value, max_value, quantity)
print(result)  # Output: [27, 148, 349, 582, 843, 950]
