from tkinter import *
from tkinter import messagebox
from random import randint, choice, sample
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
               'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
               'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

    password_len = randint(10, 15)
    symbol_count = randint(2,4)
    number_count = randint(2, 4)
    letter_count = password_len - symbol_count - number_count

    password = [choice(symbols) for _ in range(symbol_count)]
    password += [choice(numbers) for _ in range(number_count)]
    password += [choice(letters) for _ in range(letter_count)]

    password_str = ''.join(sample(password, len(password)))
    password_input.insert(0, password_str)
    pyperclip.copy(password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    json_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0:
        messagebox.showinfo(title="Empty website field", message="Oops, please fill out the website field")
    elif len(email) == 0:
        messagebox.showinfo(title="Empty email field", message="Oops, please fill out the email field")
    elif len(password) == 0:
        messagebox.showinfo(title="Empty password field", message="Oops, please fill out the password field")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Here are your details: \n\nEmail: {email} "
                                                              f"\nPassword: {password} \n\nDo you want to save?")

        if is_ok:
            try:
                with open("data.json") as file:
                    # Read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Update the file
                    json.dump(json_data, file, indent=2)
            else:
                # Update old data with new data
                data.update(json_data)

                with open("data.json", "w") as file:
                    # Update the file
                    json.dump(data, file, indent=2)
            finally:
                clear_input(website_input)
                clear_input(password_input)


def clear_input(text):
    text.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
# Create Tkinter window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=30)

# Image Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=1)

# Website input
website_label = Label(text="Website: ")
website_label.grid(row=10, column=0)
website_label.config(padx=10, pady=10)
website_input = Entry(width=45)
website_input.focus()
website_input.grid(row=10, column=1, columnspan=2)

# Email input
email_label = Label(text="Email/username: ")
email_label.grid(row=11, column=0)
email_label.config(padx=10, pady=10)
email_input = Entry(width=45)
email_input.focus()
email_input.insert(0, "safitri.shelton@gmail.com")
email_input.grid(row=11, column=1, columnspan=2)

# Password input
password_label = Label(text="Password: ")
password_label.grid(row=12, column=0)
password_label.config(padx=10, pady=10)
password_input = Entry(width=27)
password_input.focus()
password_input.grid(row=12, column=1)
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=12, column=2)

# Add button
add_btn = Button(text="Add", width=45, command=save_password)
add_btn.grid(row=13, column=1, columnspan=3)

window.mainloop()