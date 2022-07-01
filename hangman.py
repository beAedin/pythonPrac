import random
word_list = ["random", "maltesers", "eclipse"]


chosen_word = random.choice(word_list)


display = []

for i in range(1, len(chosen_word)):
    display += "_"

end = False
cnt = len(chosen_word)
while end == False:
    guess = input("Guess a letter: ").lower()

    for i in range(1, len(chosen_word)):
        el = chosen_word[i]
        if guess == chosen_word[i]:
            display[i] = el
            cnt += 1
    print(display)
    if(cnt == len(chosen_word)):
        end = True


print(display)
