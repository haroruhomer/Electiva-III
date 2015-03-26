__author__ = 'haroldhomero'

from tkinter import *
import poli
import permu


def Encriptar():
    TB_Solucion.config(state=NORMAL)
    TB_Solucion.delete(1.0, END)
    mensaje = TB_Texto.get(1.0, END)
    clavePoli = TB_ClavePoli.get()
    textoPoli = poli.Encriptar(mensaje, clavePoli)
    print(textoPoli)
    clavePermu = TB_ClavePermu.get()
    textoPermu = permu.Encriptar(textoPoli, clavePermu)
    TB_Solucion.insert(INSERT, textoPermu)
    TB_Solucion.config(state=DISABLED)


def Desencriptar():
    TB_Solucion.config(state=NORMAL)
    TB_Solucion.delete(1.0, END)
    mensaje = TB_Texto.get(1.0, END)
    clavePermu = TB_ClavePermu.get()
    textoPermu = permu.Desencriptar(mensaje, clavePermu)
    clavePoli = TB_ClavePoli.get()
    textoPoli = poli.Desencriptar(textoPermu, clavePoli)
    TB_Solucion.insert(INSERT, textoPoli)
    TB_Solucion.config(state=DISABLED)


root = Tk()
root.title('Combinado')
F_frame = Frame(root, height=600, width=800)
L_Titulo = Label(F_frame, text="encrip")
TB_Texto = Text(F_frame, height=5)
L_ClavePoli = Label(F_frame, text="Clave Poli")
TB_ClavePoli = Entry(F_frame)
L_ClavePermu = Label(F_frame, text="Clave Permu")
TB_ClavePermu = Entry(F_frame)
B_Encrip = Button(F_frame, text="Encriptar", bg="green", command=Encriptar)
B_Desencrip = Button(F_frame, text="Desencriptar", bg="red", command=Desencriptar)
TB_Solucion = Text(F_frame, height=5, state="disabled")

F_frame.grid(column=0, sticky=W + E + N + S)
L_Titulo.grid(row=0, columnspan=2)
TB_Texto.grid(row=1, columnspan=2)
L_ClavePoli.grid(row=2, sticky=E)
TB_ClavePoli.grid(row=2, column=1, sticky=W + E + N + S)
L_ClavePermu.grid(row=3, sticky=E)
TB_ClavePermu.grid(row=3, column=1, sticky=W + E + N + S)
B_Encrip.grid(row=4, column=0, sticky=W + E + N + S)
B_Desencrip.grid(row=4, column=1, sticky=W + E + N + S)
TB_Solucion.grid(row=5, columnspan=2)
root.mainloop()