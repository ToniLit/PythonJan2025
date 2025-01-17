import tkinter as tk
window = tk.Tk ()
print(window)

# # sau pui valorile direct in 
# window.geometry(f"400x600+100+150")
scr_w =window.winfo_screenwidth()
scr_y=window.winfo_screenheight()
w=h=600
x=scr_w//2- w//2
y=scr_y//2- w//2
window.geometry(f"{w}x{h}+{x}+{y}")

window.title("hello")
window.mainloop()