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

label = tk.Label(window,text="2 more days of fun")
label.pack()

labe_2=tk.Label(window,text ="what a greate day")
labe_2.pack()

counter = 0

def count():
    global counter
    print("my button pushed")
    counter += 1
    print(f"you press for {counter} times")

button = tk.Button(window, text="push me", command=count)# asa ii dai o comanda. nu trebui sa o aduci ca un parametru, dar inainte iti definesti aceasta functie
button.pack()

window.title("hello")




window.mainloop()