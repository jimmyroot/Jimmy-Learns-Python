# 8.9 - Challenge: Simulate an election
# Real Python version

from random import random

def run_regional_election(chance_A_wins):
    """Return the result of an election ("A" or "B") for a single region, specify chances of win with
    chance_A_wins
    """
    if random() < chance_A_wins:
        return "A"
    else:
        return "B"

def run_election(regional_chances):
    """Return the result of the entire election, "A" or "B".

    regional_chances is a list or tuple of floats representing the chances that candidate "A"
    will win in each regional election.
    """
    num_regions_won_by_A = 0
    for chance_A_wins in regional_chances:
        if run_regional_election(chance_A_wins) == "A":
            num_regions_won_by_A += 1

    num_regions_won_by_B = len(regional_chances) - num_regions_won_by_A
    if num_regions_won_by_A > num_regions_won_by_B:
        return "A"
    else:
        return "B"

CHANCES_A_WINS_BY_REGION = [0.87, 0.65, 0.17]
NUM_TRIALS = 10_000

# Run the simulation

num_times_A_wins = 0
for trial in range(NUM_TRIALS):
    if run_election(CHANCES_A_WINS_BY_REGION) == "A":
        num_times_A_wins += 1

# Calculate probabilities and print
print(f"Probability A wins: {num_times_A_wins / NUM_TRIALS}")
print(f"Probability B wins: {1 - (num_times_A_wins / NUM_TRIALS)}")
