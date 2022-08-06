from tkinter import *

window = Tk();
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom", expand=True); # side="left"

my_label["text"] = "updated text1"
my_label.config(text="updated text2")


# Button
def button_clicked():
    my_label.config(text=input.get())

my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()


#Entry Component
input = Entry(width=10)
input.pack()
# print(input.get())


window.mainloop()