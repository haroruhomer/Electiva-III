__author__ = 'haroldhomero'

from tkinter import messagebox


def Encriptar(mensaje, clave):
    cadena = ""
    lista = []
    listaInter = []
    listaencrip = []
    index = 0
    if ValidarClave(clave):
        modulo = (len(mensaje) - 1) % len(clave)
        print("modulo", modulo)

        for i in range(0, len(mensaje) - 1):
            cadena += mensaje[i]
        print(len(clave))

        while modulo != 0:
            cadena += " "
            modulo = (len(cadena)) % len(clave)
            print(cadena)
        numlistas = len(cadena) / len(clave)
        for j in range(0, int(numlistas)):
            print("j", j)
            for k in range(0, len(clave)):
                print("k", k)
                listaInter.append(cadena[index])
                print(index, "index", cadena[index])
                index += 1
            lista.append(listaInter)
            listaInter = []
        print(lista)

        aux = []
        for m in range(0, len(clave)):
            aux.append(' ')

        for cont in range(len(lista)):
            for l in range(0, len(clave)):
                aux[l] = lista[cont][int(clave[l])]
                print("aux____", aux)
                print("Lista+++", lista[cont])
            listaencrip.append(aux.copy())
        print(listaencrip)
        txtEncrip = "".join("".join(x) for x in listaencrip)
        return txtEncrip

    else:
        print("no valida")
    return ""


def Desencriptar(mensaje, clave):
    return ""


def ValidarClave(clave):
    validez = True
    long = len(clave)
    clavenum = 0
    try:
        clavenum = int(clave)
        for i in range(0, long - 1):
            if (str(i) not in clave):
                print(i)
                validez = False
                print(validez)
    except:
        validez = False
    return validez