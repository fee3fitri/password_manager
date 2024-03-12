import tkinter as tk
import os
import base64
import string
import random

def generate_password(length):
    while True:
        random_bytes = os.urandom(length)
        password = base64.b64encode(random_bytes).decode('utf-8')
        password = password.replace('/', '')
        password = password.replace('+', '')
        if (sum(c.isdigit() for c in password) >= 2 and
            sum(c in string.punctuation for c in password) >= 2 and
            len(password) >= 10):
            return password

def save_password(password, filename):
    with open(filename, 'a') as f:
        f.write(password + '\n')

def search_password(filename, password):
    with open(filename, 'r') as f:
        for line in f:
            if line.strip() == password:
                return True
    return False

def generate_password_button_click():
    password = generate_password(10)
    save_password(password, 'password.txt')
    password_label.config(text=password)

def search_password_button_click():
    password = search_password_entry.get()
    if search_password('password.txt', password):
        result_label.config(text='Password found!')
    else:
        result_label.config(text='Password not found!')

root = tk.Tk()
root.title('Password Manager')

generate_password_button = tk.Button(root, text='Generate Password', command=generate_password_button_click)
generate_password_button.pack()

password_label = tk.Label(root, text='')
password_label.pack()

search_password_label = tk.Label(root, text='Search Password:')
search_password_label.pack()

search_password_entry = tk.Entry(root)
search_password_entry.pack()

search_password_button = tk.Button(root, text='Search', command=search_password_button_click)
search_password_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()