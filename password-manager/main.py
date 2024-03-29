from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# JSON write : json.dump()
# JSON read : json.load()
# JSON update : json.update()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generator():
    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(numbers) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    input_pw.delete(0, END)
    input_pw.insert(0, password)

    # Clipboard
    pyperclip.copy(password)



def search():
    web = input_website.get()

    # SUCCESS
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            
            
    except FileNotFoundError:
        # ERROR
        messagebox.showerror(title=web, message="No Data File Found.")
    else:
        if web in data:
                email = data[web]["email"]
                pw = data[web]["pw"]
                messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {pw}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = input_website.get()
    email = input_email.get()
    pw = input_pw.get()
    new_data = {web: {
        "email": email,
        "pw": pw
    }}

    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail {email} \nPassword: {pw} \nIs it ok to save?")

        

        if is_ok:
            try :
                with open("data.json", "r") as f:
                    # data = f"{web} | {email} | {pw}\n"
                    # f.write(data)
                    
                    # Reading old data
                    data = json.load(f)
                    
            except FileNotFoundError:
                with open("data.json", "w") as f:
                     # Saving updated data
                    json.dump(data, f, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
            finally:
                # Clear
                input_website.delete(0, END)
                input_pw.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Canvase
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

# Label
l_website = Label(text="Website:")
l_website.grid(column=0,row=1)

l_email = Label(text="Email/Username:")
l_email.grid(column=0,row=2)

l_pw = Label(text="Password:")
l_pw.grid(column=0, row=3)

# Entry
input_website = Entry(width=30)
input_website.focus()
input_website.grid(column=1, row=1)

input_email = Entry(width=37)
input_email.insert(0, "panda01com@naver.com")
input_email.grid(column=1, row=2, columnspan=2)

input_pw = Entry(width=29)
input_pw.grid(column=1, row=3)

# Button
btn_search = Button(text="Search", command=search)
btn_search.grid(column=2, row=1)

btn_generator = Button(text="Generate", command=generator)
btn_generator.grid(column=2, row=3)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()