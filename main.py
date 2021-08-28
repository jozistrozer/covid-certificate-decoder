import tkinter as tk

# Window settings.
window = tk.Tk()
window.geometry("350x500")
window.resizable(False, False)

varHeaderText = tk.Label(text="Covid certificate decoder.")
varHeaderText.pack()


window.mainloop()
