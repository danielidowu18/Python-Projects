import art
import data
import random


def check():
    if followers_question == "a":
        global score
        global endGame
        if a_followers_amount > b_followers_amount:
            score += 1
            print(f"You're right! Current Score: {score}.")
        elif a_followers_amount < b_followers_amount:
            print(f"Sorry, that's wrong. Final score {score}")
            endGame = True
    elif followers_question == "b":
        if b_followers_amount > a_followers_amount:
            score += 1
            print(f"You're right! Current Score: {score}.")
        elif b_followers_amount < a_followers_amount:
            print(f"Sorry, that's wrong. Final score {score}")
            endGame = True

endGame = False
score = 0
while not endGame:
    print(art.logo)
    length_of_data = len(data.details)
    first_data = data.details[random.randrange(length_of_data)]
    second_data = data.details[random.randrange(length_of_data)]
    print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}")
    print(art.vs)
    print(f"Against B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}")
    a_followers_amount = first_data['follower_count']
    b_followers_amount = second_data['follower_count']
    followers_question = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()
    check()