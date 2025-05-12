from tkinter import *
window = Tk()
window.geometry("750x400")
window.title("Currency converter")
window.config(background="RED")

def from_dollar():
    pound= float(input_value.get())*0.76

    euro= float(input_value.get())*0.90

    pesos= float(input_value.get())*19.60





dollar = Label(window,text="Dollars")

input_value = IntVar() # Entry box datatype
dollarInp = Entry(window,textvariable= input_value)
input_value
pound = Label(window,text="Pound")
euro = Label(window,text="Euro")
pesos = Label(window,text="Pesos")

conv_button = Button(window,text="Convert",bd = 7,bg="blue",
                    fg="WHITE",command=None)


poundconv = Text(window,height = 3, width = 20)
pesosconv = Text(window,height = 3, width = 20)
euroconv = Text(window,height = 3, width = 20)

dollar.grid(row=0,column=0,pady=15)
dollarInp.grid(row=0,column=2,pady=15,padx = 15)
conv_button.grid(row=0,column=3,pady=15)

pesos.grid(row=3,column=3,pady=15)
euro.grid(row=3,column=5,pady=15)
pound.grid(row=3,column=1,pady=15)

poundconv.grid(row=3,column=2,pady=15)
euroconv.grid(row=4,column=5,pady=15)
pesosconv.grid(row=4,column=3,pady=15)







window.mainloop()
