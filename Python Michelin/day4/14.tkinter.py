import tkinter as tk
from tkinter import messagebox
import time
import random



I_AM_NOT_HUNGRY = "I_AM_NOT_HUNGRY"
B= "I_AM_NOT_HUNGRY"
D= "Dont't feed me"
E= "Feed Me"
I_am_happy="I AM Happy"

win_size= 500

main_win = tk.Tk()

status_label = tk.Label(main_win, text= I_AM_NOT_HUNGRY)
status_label.pack()

def give_food():
    global is_gam_runni
    if not is_gam_runni:
        return
    print("give me food")
    # doar citim aceasta variabila
    if is_hungry:
        print("you win")
        stop_time = time.time()
        delta= stop_time - start_time
        messagebox.showinfo(title="felicitari!!",message= {"Ai castigat in",(delta)})
        # status_label.config(text=I_am_happy)
        # feed_butt.columnconfigure(text=D)
    else:
        print("you lose")
        messagebox.showerror(title="uuuuu",message="ai pierdut prietene")
    is_gam_runni = False
    
is_hungry = False

is_gam_runni= True

def I_am_h():
    global is_hungry
    #vrem sa schimbam aceasta variabila
    print("Mancare nu e buna")
    status_label.config(text=B)
    feed_butt.config(text=E)
    is_hungry = True

feed_butt=tk.Button(main_win, text=D, command=give_food)
feed_butt.pack()

main_win.geometry(f"{win_size}x{win_size}")
main_win.title("Statusul_Zilei")

status_label.after(3000,I_am_h)
start_time=time.time()

main_win.mainloop()