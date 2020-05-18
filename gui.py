import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.config(font=("Courier", 44))
greeting.pack()
window.mainloop()