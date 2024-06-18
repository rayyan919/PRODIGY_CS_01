import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from caeser_cipher_Prodigy_Task01 import caeser_cipher

def encrypt_text():
    text = text_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caeser_cipher(text, shift, encrypt=True)
    result_label.config(text=f"Encrypted Text: {encrypted_text}")


def decrypt_text():
    ciphertext = text_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caeser_cipher(ciphertext, shift, encrypt=False)
    result_label.config(text=f"Decrypted Text: {decrypted_text}")


def validate_shift_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False


root = tk.Tk()
root.title("Caesar Cipher")


image = Image.open("background_image.webp")
image = image.resize((1600, 914), Image.LANCZOS)  # Resize the image to 1600x914
background_image = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root, width=1600, height=914)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=background_image)


canvas.create_text(800, 50, text="Welcome to Caesar Cipher", fill="white", font=("Arial", 24, "bold"), anchor="center")


canvas.create_text(600, 150, text="Enter Text:", fill="white", font=("Arial", 14, "bold"), anchor="e")
text_entry = ttk.Entry(root, width=50)
canvas.create_window(850, 150, window=text_entry, anchor="center")


vcmd = (root.register(validate_shift_input), '%P')

canvas.create_text(600, 200, text="Shift Value (Only accepts integer values):", fill="white", font=("Arial", 14, "bold"), anchor="e")
shift_entry = ttk.Entry(root, width=10, validate="key", validatecommand=vcmd)
canvas.create_window(850, 200, window=shift_entry, anchor="center")

encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_text)
canvas.create_window(700, 250, window=encrypt_button, anchor="center")

decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_text)
canvas.create_window(1000, 250, window=decrypt_button, anchor="center")

result_label = ttk.Label(root, text="Result: ", background="white")
canvas.create_window(850, 300, window=result_label, anchor="center")


root.mainloop()
