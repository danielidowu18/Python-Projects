import random
logo = '''

 _____ _                __                 _                   ___                     _                 ___                     
/__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __    / _ \_   _  ___  ___ ___(_)_ __   __ _    / _ \__ _ _ __ ___   ___ 
  / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |  / /_\/ _` | '_ ` _ \ / _ \ 
 / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |    / /_\\| |_| |  __/\__ \__ \ | | | | (_| | / /_\\ (_| | | | | | |  __/
 \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    \____/ \__,_|\___||___/___/_|_| |_|\__, | \____/\__,_|_| |_| |_|\___|                                                                                               |___/                             
'''
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
numbers = []
for n in range(1, 101):
    numbers.append(n)
computerChoice = random.choice(numbers)
# print(f"Psst, the answer is {computerChoice}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
def check(userGuess, computerChoice):
    global noOfAttempts
    global endGame
    if userGuess == computerChoice:
        print(f"You got it! The answer was {userGuess}.")
        endGame = True
    elif noOfAttempts == 1:
        print(f"You're out of attempts. The answer is {computerChoice}")
        endGame = True
    elif userGuess > computerChoice:
        noOfAttempts -= 1   
        print("Too high.\nGuess again.")
        print(f"You have {noOfAttempts} attempts remaining to guess the number.")
    elif userGuess < computerChoice:
        noOfAttempts -= 1        
        print("Too low.\nGuess again.")
        print(f"You have {noOfAttempts} attempts remaining to guess the number.")
     
if difficulty == "easy":
    noOfAttempts = 10
    print(f"You have {noOfAttempts} attempts remaining to guess the number.")
    endGame = False    
    while not endGame:
        userGuess = int(input("Make a guess: "))
        check(userGuess, computerChoice)

elif difficulty == "hard":
    noOfAttempts = 5
    print(f"You have {noOfAttempts} attempts remaining to guess the number.")
    endGame = False    
    while not endGame:
        userGuess = int(input("Make a guess: "))
        check(userGuess, computerChoice)