from tkinter import *

# Entry => Label (miles -> km)
def convert():
    res = round(float(input.get())*1.609)
    label_result.config(text=f"{res}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200,100)
window.config(padx=20,  pady=20)


# Input
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
label_miles = Label(text="Miles");
label_miles.grid(column=2, row=0)

label_is = Label(text="is equal to")
label_is.grid(column=0, row=1)

label_km = Label(text="km")
label_km.grid(column=2, row=1)

label_result = Label(text=0)
label_result.grid(column=1,row=1)


# Button
btn = Button(text="Calculate", command=convert)
btn.grid(column=1, row=2)




window.mainloop()