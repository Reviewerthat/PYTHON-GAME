from tkinter import *
window = Tk()
window.geometry("750x400")
window.title("Currency converter")
window.config(background="RED")

def from_dollar():
    pound= float(input_value.get()) *0.76

    euro= float(input_value.get()) * 0.91

    pesos= float(input_value.get()) * 19.60


    poundconv.delete("1.0",END)
    poundconv.insert(END, pound)

    euroconv.delete("1.0",END)
    euroconv.insert(END, euro)

    poundconv.delete("1.0",END)
    pesosconv.insert(END, pesos)



dollar = Label(window,text="Dollars")

input_value = IntVar() # Entry box datatype
dollarInp = Entry(window,textvariable= input_value)
input_value
poundlab = Label(window,text="Pound")
eurolab = Label(window,text="Euro")
pesoslab = Label(window,text="Pesos")

conv_button = Button(window,text="Convert",bd = 7,bg="blue",
                    fg="WHITE",command=from_dollar)




poundconv = Text(window,height = 3, width = 20)
pesosconv = Text(window,height = 3, width = 20)
euroconv = Text(window,height = 3, width = 20)

dollar.grid(row=0,column=0,pady=15)
dollarInp.grid(row=0,column=2,pady=15,padx = 15)
conv_button.grid(row=0,column=3,pady=15)

pesoslab.grid(row=3,column=3,pady=15)
eurolab.grid(row=3,column=5,pady=15)
poundlab.grid(row=3,column=1,pady=15)

poundconv.grid(row=3,column=2,pady=15)
euroconv.grid(row=4,column=5,pady=15)
pesosconv.grid(row=4,column=3,pady=15)







window.mainloop()
