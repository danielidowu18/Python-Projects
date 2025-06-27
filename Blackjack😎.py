import random

playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
if playGame == "y":
    print(logo)

while playGame == "y":
    userCards = random.choices(cards, k=2)
    userScore = sum(userCards)
    computerCards = random.choices(cards, k=2)
    computerScore = sum(computerCards)
    userFinalCard = random.choice(cards)
    computerFinalCard = random.choice(cards)
    def judge(userScore, computerScore):
        if userScore > 21:    
           print("You went over. You lose.")
        elif computerScore > 21:
            print("Computer went over. You Win.")
        elif userScore > computerScore:
            print("Congratulations, You win.")
        elif userScore < computerScore:
            print("You lose.")
        elif userScore == computerScore:
            print("You drew.")        
    print(f"Your cards: {userCards}, current score: {userScore}")
    print(f"Computer's first card: {computerCards[0]}")
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if get_another_card == "y":
        userCards.append(userFinalCard)
        userScore = sum(userCards)
        if userScore > 21:
            if userCards[2] == 11:
                userScore -= 10
        if computerScore <= 16 and userScore <= 21:
            computerCards.append(computerFinalCard)
            computerScore = sum(computerCards)      
        if computerScore > 21:
            if computerCards[2] == 11:
                computerScore -= 10            
        print(f"Your cards: {userCards}, current score: {userScore}")
        print(f"Computer's first card: {computerCards[0]}")
        print(f"Your final hand: {userCards}, final score: {userScore}")
        print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
        judge(userScore, computerScore)
        playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    elif get_another_card == "n":
        if userScore > 21:
            if userCards[1] == 11:
                userScore -= 10
        if computerScore > 21:
            if computerCards[2] == 11:
                computerScore -= 10
        print(f"Your final hand: {userCards}, final score: {userScore}")
        print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
        judge(userScore, computerScore)
        playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
