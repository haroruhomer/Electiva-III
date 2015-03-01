__author__ = 'haroldhomero'

from tkinter import *
import permu


def Encriptar():
    TB_Solucion.config(state=NORMAL)
    TB_Solucion.delete(1.0, END)
    mensaje = TB_Texto.get(1.0, END)
    clave = TB_Clave.get()
    texto = permu.Encriptar(mensaje, clave)
    TB_Solucion.insert(INSERT, texto)
    TB_Solucion.config(state=DISABLED)


def Desencriptar():
    TB_Solucion.config(state=NORMAL)
    TB_Solucion.delete(1.0, END)
    mensaje = TB_Texto.get(1.0, END)
    clave = TB_Clave.get()
    texto = permu.Desencriptar(mensaje, clave)
    TB_Solucion.insert(INSERT, texto)
    TB_Solucion.config(state=DISABLED)


root = Tk()
root.title('Permutación')
F_frame = Frame(root, height=600, width=800)
L_Titulo = Label(F_frame, text="encrip")
TB_Texto = Text(F_frame, height=5)
L_Clave = Label(F_frame, text="Clave")
TB_Clave = Entry(F_frame)
B_Encrip = Button(F_frame, text="Encriptar", bg="green", command=Encriptar)
B_Desencrip = Button(F_frame, text="Desencriptar", bg="red", command=Desencriptar)
TB_Solucion = Text(F_frame, height=5, state="disabled")

F_frame.grid(column=0, sticky=W + E + N + S)
L_Titulo.grid(row=0, columnspan=2)
TB_Texto.grid(row=1, columnspan=2)
L_Clave.grid(row=2, sticky=E)
TB_Clave.grid(row=2, column=1, sticky=W + E + N + S)
B_Encrip.grid(row=3, column=0, sticky=W + E + N + S)
B_Desencrip.grid(row=3, column=1, sticky=W + E + N + S)
TB_Solucion.grid(row=4, columnspan=2)
root.mainloop()