from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_dict = {}

########### READ CSV ###########

try:
    data = pandas.read_csv("data/esperanto.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/esperanto.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

########## CARD ###########


def next_card():
    # appear esperanto_word
    # recall flip_card


    global current_card, flip_timer

    # Reset flip_timer
    window.after_cancel(flip_timer)

    # randomly choose from word list
    current_card = random.choice(word_dict)

    # draw on canvas [esperanto_word]
    canvas.itemconfig(title, text="Esperanto", fill="black")
    canvas.itemconfig(word, text=current_card["Esperanto"], fill="black")

    # Recall flip_timer
    window.after(3000, func=flip_card)



########## 3000ms->flip ##########
def flip_card():
    canvas.itemconfig(title, text="English", fill="green")
    canvas.itemconfig(word, text=current_card["English"], fill="green")
    canvas.itemconfig(card_background, image=card_back)


########## Correct ###########
def know_word():
    # Remove cur_card from cur_data
    word_dict.remove(current_card)

    # Make a dataframe -> csv
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/memorize_word_list", index=False)

    next_card()


########### UI ############
window = Tk();
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

card_background = PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263, image=card_background)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title = canvas.create_text(400, 150, text="Esperanto", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="English", font=("Ariel", 60, "bold"))
canvas.grid(column=0,row=0, columnspan=2)

#Button
img_btn_right = PhotoImage(file="images/right.png")
img_btn_wrong = PhotoImage(file="images/wrong.png")


btn_right = Button(image=img_btn_right, highlightthickness=0, command=know_word)
btn_right.grid(column=0, row=1)

btn_wrong = Button(image=img_btn_wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(column=1, row=1)



next_card()
window.mainloop()