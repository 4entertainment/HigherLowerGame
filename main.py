from art import logo, vs
import random
from game_data import data

"""
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
"""


def make_dict(data):
    random_dict = random.choice(data)
    # follower_count = random_dict['follower_count']
    return random_dict


def calculate_winner(dict1, dict2):
    if dict1['follower_count'] > dict2['follower_count']:
        winner = dict1['name']
        return winner
    else:
        winner = dict2['name']
        return winner


def game_on():
    total_score = 0

    while True:
        print(logo)
        choice_a = make_dict(data)
        choice_b = make_dict(data)
        print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']}.")
        print(vs)
        print(f"Against B: {choice_b['name']}, {choice_b['description']}, from {choice_b['country']}.")

        input_choice = input("Who has more followers? Type 'A' or 'B': ")
        if input_choice == 'A' or input_choice == 'a':
            input_winner = choice_a['name']
        elif input_choice == 'B' or input_choice == 'b':
            input_winner = choice_b['name']
        winner = calculate_winner(choice_a, choice_b)
        if winner == input_winner:
            total_score += 1
            print(f"You're right! Current score: {total_score}.")
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {total_score}")
            break



game_on()
