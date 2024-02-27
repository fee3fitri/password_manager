from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Create Tkinter window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Image Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=1)

# Website input
website_label = Label(text="Website: ")
website_label.grid(row=10, column=0)
website_label.config(padx=10, pady=10)
website_input = Entry(width=50)
website_input.grid(row=10, column=1, columnspan=2)

# Email input
email_label = Label(text="Email/username: ")
email_label.grid(row=11, column=0)
email_label.config(padx=10, pady=10)
email_input = Entry(width=50)
email_input.grid(row=11, column=1, columnspan=2)

# Password input
password_label = Label(text="Password: ")
password_label.grid(row=12, column=0)
password_label.config(padx=10, pady=10)
password_input = Entry(width=30)
password_input.grid(row=12, column=1)
password_btn = Button(text="Generate Password")
password_btn.grid(row=12, column=2)

# Add button
add_btn = Button(text="Add", width=50)
add_btn.grid(row=13, column=1, columnspan=3)

window.mainloop()
