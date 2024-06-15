import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Encrypt and Decrypt')
root.geometry('1920x1080')
text = ttk.Label(root, text="Enter Text:")
text.place(anchor= 'center', relx = 0.5, rely = 0.3)
text_entry = ttk.Entry(root, width=50)
text_entry.place(anchor = 'center', relx = 0.5, rely = 0.35)
root.mainloop()
