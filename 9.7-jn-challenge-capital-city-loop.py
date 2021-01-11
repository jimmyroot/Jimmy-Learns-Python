import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    }
# This was my original version...

# choice = random.choice(list(capitals_dict.keys()))
# state = choice
# city = (capitals_dict[choice]).lower()

# However this is a more succint version using list unpacking

state, city = random.choice(list(capitals_dict.items()))


# Again here is my original version...

# user_answer = (input(f"The state is {state}, now you enter the capital: ")).lower()

# while not (user_answer == city or user_answer.lower() == "exit"):
#     user_answer = input("I'm afraid that's incorrect, please try again or type 'exit' to quit: ")

# if user_answer.lower() == city.lower():
#     print(f"Correct!")
# else:
#    print(f"The correct answer was {city.capitalize()}! Goodbye.")

# And the more succint version from the example, notice how all the code is encapsulated
# inside the loop unlike my own where I only looped for matching input...

while True:
    guess = input(f"The state is {state}, now you enter the capital: ").lower()
    if guess == "exit":
        print(f"The correct answer was '{city}'.")
        print("Goodbye!")
        break
    elif guess == city.lower():
        print("Correct! Well done!")
        break
