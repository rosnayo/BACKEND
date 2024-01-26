from tkinter import *
from tkinter import messagebox

def saludar():
    messagebox.showinfo("mensaje","hola " + txt_nombre.get())

#crear un objeto de la clase Tk()
app = Tk()
app.geometry('300x100')
app.title('Mi pimer App con Tk')

#agregar un frame
frame = LabelFrame(app,text='Nueva Ventana')
frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)

#agregamos un label
lb_nombre = Label(frame,text='Nombre : ')
lb_nombre.grid(row=1,column=0)
#agregamos una textbox
txt_nombre = Entry(frame)
txt_nombre.grid(row=1,column=1)
#agregamos un boton
btn_saludo = Button(frame,text='saludar',command=saludar)
btn_saludo.grid(row=1,column=2)

app.mainloop()
