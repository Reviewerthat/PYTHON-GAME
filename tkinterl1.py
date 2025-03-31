from tkinter import *
root = Tk()

root.geometry("500x600")
btn = Button(root,text = "Click me",background="blue",bd = 10,activeforeground="pink",activebackground="green",command = root.destroy)

btn.pack(side="top")



root.mainloop()
