import random
import hangmanArt
import hangmanWords
print(hangmanArt.logo)
word_list = hangmanWords.words
chosen_word = random.choice(word_list)
display = []
for _ in chosen_word:
    display += "_"
print(display)
lives = 6
endGame = False
while endGame == False:
    guess = (input("Guess a letter: ")).lower()
    if guess in display:
            print(f"You have chosen {guess} already")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            if "_" not in display:
                endGame = True
                print("You win!")
                
    if guess not in chosen_word:
        print(hangmanArt.status[lives - 1])
        print(f"{guess} is not in the word, You lose a life")
        lives -= 1
        if lives == 0:
            endGame = True
            display = chosen_word
            print(f"You lose")
    print(f"{' '.join(display)}")                     
# l = 0
# while l < len(chosen_word):
#     if guess in chosen_word[l]:
#         print("right")
#     else:
#         print("false")
#     l += 1        
# OR
# for alpha in chosen_word:
#     if alpha == guess:
#         print("Right")
#     else:
#         print("False")     
