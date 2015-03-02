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
        for i in range(0, len(mensaje) - 1):
            cadena += mensaje[i]
        while modulo != 0:
            cadena += " "
            modulo = (len(cadena)) % len(clave)
        numlistas = len(cadena) / len(clave)
        for j in range(0, int(numlistas)):
            print("j", j)
            for k in range(0, len(clave)):
                listaInter.append(cadena[index])
                index += 1
            lista.append(listaInter)
            listaInter = []
        aux = []
        for m in range(0, len(clave)):
            aux.append(' ')

        for cont in range(len(lista)):
            for l in range(0, len(clave)):
                aux[l] = lista[cont][int(clave[l])]
            listaencrip.append(aux.copy())
        txtEncrip = "".join("".join(x) for x in listaencrip)
        return txtEncrip

    else:
        print("no valida")
    return ""


def Desencriptar(mensaje, clave):
    cadena = ""
    lista = []
    listaInter = []
    listaencrip = []
    index = 0
    if ValidarClave(clave):
        modulo = (len(mensaje) - 1) % len(clave)
        for i in range(0, len(mensaje) - 1):
            cadena += mensaje[i]
        while modulo != 0:
            cadena += " "
            modulo = (len(cadena)) % len(clave)
        numlistas = len(cadena) / len(clave)
        for j in range(0, int(numlistas)):
            print("j", j)
            for k in range(0, len(clave)):
                listaInter.append(cadena[index])
                index += 1
            lista.append(listaInter)
            listaInter = []
        aux = []
        for m in range(0, len(clave)):
            aux.append(' ')
        for cont in range(len(lista)):
            for l in range(0, len(clave)):
                aux[l] = lista[cont][int(clave[l])]
            listaencrip.append(aux.copy())
        txtEncrip = "".join("".join(x) for x in listaencrip)
        return txtEncrip

    else:
        print("no valida")

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