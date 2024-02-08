#Tsygankov_FP_7

import random

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(num_trials):
        dice1 = roll_dice()
        dice2 = roll_dice()
        results[dice1 + dice2] += 1
    
    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for key, value in probabilities.items():
        print(f"{key}\t{value:.2f}% ({value/100:.2f})")

def main():
    num_trials = 1000000
    probabilities = monte_carlo_simulation(num_trials)
    print_probabilities(probabilities)

if __name__ == "__main__":
    main()
