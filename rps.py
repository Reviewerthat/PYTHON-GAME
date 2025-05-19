from tkinter import *
import random
import tkinter.font as font

player_score = 0
computer_score = 0
options = [("rock",0),("paper",1),("scissors",2)]



#main window
window = Tk()
window.geometry("700x400")
window.title("RPS Game")
window.config(background="BLUE")
app_font = font.Font(size=20)

#game title
game_title = Label(window,text = "Rock Paper Scissors",bg="black",fg="white",font=app_font)
game_title.pack()


#who wins the game
winner_label = Label(text="Lets start the game",bg="black",fg="white",font = font.Font(size=15),pady=8)
winner_label.pack()

input_frame = Frame(window,bg="brown")
input_frame.pack()

#display player options

player_option = Label(input_frame,text="Your Option",font = font.Font(size=15),bg="BROWN",fg="white")
player_option.grid(row=0,column=0,pady=10)

window.mainloop()
