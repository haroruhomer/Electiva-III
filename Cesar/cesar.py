__author__ = 'haroldhomero'
import utilitarios

abc=utilitarios.Cargar()

def Encriptar(mensajeO, clave):

    encrip = ""

    for letra in mensajeO:
        aux=0
        for i in range(0,len(abc)):
            if letra==abc[i]:
                pos=(i+clave)%len(abc)
                letraEncrip=abc[pos]
                print(letraEncrip)
                encrip+=letraEncrip
                aux=1
        if aux==0:
            encrip+=letra
    return encrip

def Desencriptar(mensajeO, clave):

    desencrip=""

    for letra in mensajeO:
        aux=0
        for i in range(0, len(abc)):
            if letra==abc[i]:
                total=i-clave
                while total<0:
                    print(len(abc))
                    total+=len(abc)
                pos=total%len(abc)
                letradesencrip=abc[pos]
                desencrip+=letradesencrip
                aux=1
        if aux==0:
            desencrip+=letra
    return desencrip