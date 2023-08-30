import random


def get_random_winners(quantity, participants):
    if quantity > len(participants):
        # Not enough participants for the requested quantity of winners
        return []

    # Create a copy of the participants list
    winners = participants.copy()

    # Shuffle the winners list in place
    random.shuffle(winners)
    # Select the desired quantity of random winners
    sample_winners = random.sample(winners, k=quantity)

    return sample_winners


# Example usage
participants_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
num_winners = 2
random_winners = get_random_winners(num_winners, participants_list)
print(random_winners)  # Output: A list of randomly selected winners
