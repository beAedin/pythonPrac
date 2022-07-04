import random
import hangman_words
import hangman_art
word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

lives = 6
chosen_word = random.choice(word_list)
display = []
end_of_game = False

word_length = len(chosen_word)

for i in range(word_length):
    display += "_"


print(logo)
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    for i in range(0, len(chosen_word)):
        el = chosen_word[i]
        if guess == el:
            display[i] = el
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose!")
            end_of_game = True

    # display does not include "_"
    if "_" not in display:
        end_of_game = True
        print("Finished")
