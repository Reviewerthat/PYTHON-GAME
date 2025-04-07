from tkinter import *
win = Tk()
win.geometry("600x500") #or minsize
win.title("Log In Layout")
win.config(background="orange")
#lables for username and pass
username = Label(win,text="Username",
                    bg = "purple").place(x =60, y=60)

password = Label(win,text="Password",bg = "yellow").place(x=60, y=90)

# input area / entrylabels
username_input_area = Entry(win,width = 20).place(x=140,y=60)
user_password_entry_area = Entry(win,width=20,show="*").place(x=140, y=90)

#submit button
btn = Button(win,text="Submit",bg="red",
                bd = 1).place(x=60,y=130)












win.mainloop()
