from tkinter import *
import random
import tkinter.font as font


player_score = 0
computer_score = 0
options = [("rock",0),("paper",1),("scissors",2)]


def comp_wins():
    global player_score, computer_score
    computer_score = computer_score + 1
    winner_label.config(text="Computer won")
    computer_score_lbl.config(text="Computer Score: "+str(computer_score))
    player_score_lbl.config(text="Player Score: "+ str(player_score))

def player_wins():
    global player_score, computer_score
    player_score = player_score + 1
    winner_label.config(text="Player won")
    computer_score_lbl.config(text="Computer Score: "+str(computer_score))
    player_score_lbl.config(text="Player Score: "+ str(player_score))

def tie():
    global player_score, computer_score
    winner_label.config(text="There was a tie!")
    computer_score_lbl.config(text="Computer Score: "+str(computer_score))
    player_score_lbl.config(text="Player Score: "+ str(player_score))

def get_computer_choice():
    return random.choice(options)

#get player input

def get_player_choice(player_input):
    global player_score, computer_score
    print(player_input)
    comp_input = get_computer_choice()
    print(comp_input)
    player_choice_lbl.config(fg="pink",text="You selected: "+player_input[0])
    computer_choice_lbl.config(fg="pink",text="You selected: "+comp_input[0])
    
    

    













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
#text rocck button
rock_btn = Button(input_frame, text="Rock",width=17,bd=4.5,bg="Blue",
            pady=10,padx=10,command=None)
#rock
rock_btn.grid(row=1,column=1,padx=10,pady=5)


#text_paper button
paper_btn = Button(input_frame, text="Paper",width=17,bd=4.5,bg="Blue",
            pady=10,padx=10,command=None)
#paper
paper_btn.grid(row=1,column=2,padx=10,pady=5)


#scissors_paper button
scissors_btn = Button(input_frame, text="Scissors",width=17,bd=4.5,bg="Blue",
            pady=10,padx=10,command=None)
#scissors
scissors_btn.grid(row=1,column=3,padx=10,pady=5)

#displaying sccore and player choice

score_lbl = Label(input_frame,text="Score: ", font =app_font,
                bg="Pink",fg="white"    )
score_lbl.grid(row=2,column=0)

player_choice_lbl = Label(input_frame,text="You selected: ----",bg="red",
                font=app_font)
player_choice_lbl.grid(row=3,column=1,pady =5)

player_score_lbl = Label(input_frame,text="Your scored: ",bg="red",
            font=app_font)
player_score_lbl.grid(row=3,column=3)

computer_choice_lbl = Label(input_frame,text="Computer selected: --- ",bg="red",
            font=app_font)
computer_choice_lbl.grid(row=4,column=1,pady=5)

computer_score_lbl = Label(input_frame,text="Computer scored: ",bg="red",
            font=app_font)
computer_score_lbl.grid(row=4,column=3)


 






window.mainloop()
