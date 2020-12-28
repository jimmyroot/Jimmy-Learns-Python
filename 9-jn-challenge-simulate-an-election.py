import random

num_simulations = 10_000
num_wins = 0
num_losses = 0

def region_1_vote(chance_of_winning):
    if random.random() < chance_of_winning:
        return 1
    else:
        return 0

def region_2_vote(chance_of_winning):
    if random.random() < chance_of_winning:
        return 1
    else:
        return 0

def region_3_vote(chance_of_winning):
    if random.random() < chance_of_winning:
        return 1
    else:
        return 0

def simulation():
    vote_result = region_1_vote(.87) + region_2_vote(.65) + region_3_vote(.17)
    if vote_result >= 2:
        return True
    else:
        return False

    
for result in range(num_simulations):
    if simulation() == True:
        num_wins += 1
    else:
        num_losses += 1

candidate_a_chance = num_wins / num_simulations
candidate_b_chance = num_losses / num_simulations
print(f"There is a {candidate_a_chance:.2%} chance that Candidate A will win.")
print(f"There is a {candidate_b_chance:.2%} chance that Candidate B will win.")
