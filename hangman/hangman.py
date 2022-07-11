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

guessed_list = []
isGuessed = False

print(logo)
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    isGuessed = False

    # they've already guessed, let them know the word
    # for i in range(0, len(guessed_list)):
    #     if guess == guessed_list[i]:
    #         isGuessed = True

    if guess in display:
        print(f"You've already guessed {guess}")
    # if isGuessed == True:
    #     print("input again\n")
    #     continue

    guessed_list.append(guess)

    for i in range(0, len(chosen_word)):
        el = chosen_word[i]

        if guess == el:
            display[i] = el

    print(f"{' '.join(display)}\n")
    print(stages[lives])
    if guess not in chosen_word:
        lives -= 1

        print(f"You guessed {guess}. That's not in the word\n")
        if lives == 0:
            print("You lose!")
            end_of_game = True

    # display does not include "_"
    if "_" not in display:
        end_of_game = True
        print("\nFinished!!")
