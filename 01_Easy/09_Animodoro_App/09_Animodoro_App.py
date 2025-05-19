#Addin libraries
import tkinter as tk
import pygame

#Let's make it simple with one main window and two layer, three buttons

#creating the window
window = tk.Tk()
window.title("Animodoro 50/10")
window.geometry("200x180")
window.resizable(False, False)



#creating the main window
frame = tk.Frame(window)
frame.pack()

#Let's add the counter in the (0,0)
counter_frame = tk.Label(frame, text="time")
counter_frame.grid(row=0, column=0, padx=20, pady=20)

#Let's add the buttons in the (1.0)
button_frame = tk.Label(frame, text="buttons")
button_frame.grid(row=1, column=0, padx=20, pady=20)

#Add buttons
timer_running =False
play_btn = tk.Button(button_frame, text="▶️", command=toggle_timer, bg="#98FB98")
play_btn.pack()
pause_btn = tk.Button(button_frame, text="⏸️", command=toggle_timer, bg="#98FB98")
pause_btn.pack()
reset_btn = tk.Button(button_frame, text="🔄", command = toggle_timer, bg="#98FB98")
reset_btn.pack()

window.mainloop()