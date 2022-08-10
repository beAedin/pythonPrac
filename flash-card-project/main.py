from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


########### CSV ###########

data = pandas.read_csv("data/esperanto.csv")
# match eo-en
word_dict = data.to_dict(orient="records")

########## CARD ###########

def next_card():
    current_card = random.choice(word_dict)
    print(current_card["Esperanto"])
    canvas.itemconfig(text_eo, text="Esperanto")
    canvas.itemconfig(text_en, text=current_card["Esperanto"])


########### UI ############
window = Tk();
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
# card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

text_eo = canvas.create_text(400, 150, text="Esperanto", font=("Ariel", 40, "italic"))
text_en = canvas.create_text(400, 263, text="English", font=("Ariel", 60, "bold"))
canvas.grid(column=0,row=0, columnspan=2)

#Button
img_btn_right = PhotoImage(file="images/right.png")
img_btn_wrong = PhotoImage(file="images/wrong.png")


btn_right = Button(image=img_btn_right, highlightthickness=0, command=next_card)
btn_right.grid(column=0, row=1)

btn_wrong = Button(image=img_btn_wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(column=1, row=1)



next_card()
window.mainloop()