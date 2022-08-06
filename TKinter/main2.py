from tkinter import *

# pack과 grid는 같은 프로그램에서 사용 불가

def button_clicked():
    my_label.config(text=input.get())


window = Tk();
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

my_label["text"] = "updated text1"
my_label.config(text="updated text2")

my_label.pack(side="bottom", expand=True); # side="left" "right"
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0);

# Button
my_button = Button(text="Click Me", command=button_clicked)
#my_button.pack()
my_button.grid(column=1, row=1)



#Entry Component
input = Entry(width=10)
# print(input.get())
# input.pack()
input.grid(column=3, row=3)

# New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

window.mainloop()