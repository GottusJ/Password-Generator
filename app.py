import random
import customtkinter as tk
import pyperclip as py

# Application's Appearance and Color Theme
tk.set_appearance_mode("system")
tk.set_default_color_theme("green")

# App Frame
app = tk.CTk()
app.geometry("750x400")
app.title("Password Generator")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890/?"

# Inputs and Variables
title = tk.CTkLabel(app, text="Password Generator", font=("none", 30))
label = tk.CTkLabel(app, font=("none", 25))
copy = tk.CTkLabel(app, text="Password was copied to clipboard", text_color="green")


# Generator
def psw_gen():
    number = 1
    length = 10

    for n in range(number):
        password = ""
        for l in range(length):
            password += random.choice(chars)

    label.configure(text=f"Password: \n{password}")
    label.pack(padx=10, pady=12)
    copy.pack()

    py.copy(password)


button = tk.CTkButton(
    app, text="Generate", command=psw_gen, font=("none", 20), width=150, height=75
)

# App Display
title.pack(padx=10, pady=50, anchor="center")
button.pack(padx=20, pady=20, anchor="center")

app.mainloop()
