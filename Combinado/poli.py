__author__ = 'haroldhomero'
import utilitarios

abc = utilitarios.Cargar()


def Encriptar(mensajeO, clave):
    posclave = 0
    numclave = 0
    encrip = ""
    if EvaluaClave(clave):
        for letra in mensajeO:
            for j in range(0, len(abc) - 1):
                if clave[posclave] == abc[j]:
                    if posclave == (len(clave) - 1):
                        posclave = 0
                    else:
                        posclave += 1
                    numclave = j
                    break
            aux = 0
            for i in range(0, len(abc) - 1):
                if letra == abc[i]:
                    pos = (i + numclave) % len(abc)
                    encrip += abc[pos]
                    aux = 1
            if aux == 0:
                encrip += letra
    print(encrip)
    return encrip


def Desencriptar(mensajeO, clave):
    posclave = numclave = 0
    desencrip = ""
    if EvaluaClave(clave):
        for letra in mensajeO:
            for j in range(0, len(abc) - 1):
                if clave[posclave] == abc[j]:
                    if posclave == len(clave) - 1:
                        posclave = 0
                    else:
                        posclave += 1
                    numclave = j
                    break

            aux = 0
            for i in range(0, len(abc) - 1):
                if letra == abc[i]:
                    total = i - numclave
                    while total < 0:
                        total += len(abc)
                    pos = total % len(abc)
                    desencrip += abc[pos]
                    aux = 1

            if aux == 0:
                desencrip += letra
    return desencrip


def EvaluaClave(clave):
    print(abc)
    cont = 0
    validez = True
    for letra in clave:
        for i in range(0, len(abc)):
            if letra != abc[i]:
                cont += 1
        if cont == (len(abc)):
            validez = False
            break
        cont = 0
    return validez