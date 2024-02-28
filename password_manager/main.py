from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    with open("password_manager.txt", mode="a") as file:
        file.write(f"\n{website} | {email} | {password}")


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
password_btn = Button(text="Generate Password")
password_btn.grid(row=12, column=2)

# Add button
add_btn = Button(text="Add", width=45, command=save_password)
add_btn.grid(row=13, column=1, columnspan=3)

window.mainloop()
