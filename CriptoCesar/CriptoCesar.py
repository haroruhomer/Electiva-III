__author__ = 'haroldhomero'
import utilitarios

abc=utilitarios.Cargar()

def Analizar(mensajeO):

    mayorN=0;
    for letra in mensajeO:
        if  mensajeO.count(letra)>mayorN:
            mayorN=mensajeO.count(letra)
            print(letra," ",mensajeO.count(letra))
            mayorC=letra
    for i in range(len(abc)):
        if abc[i]==mayorC:
            clave=i
            print(clave)

    desencrip=""

    for letra in mensajeO:
        aux=0
        for i in range(0, len(abc)):
            if letra==abc[i]:
                total=i-clave
                while total<0:
                    total+=len(abc)
                pos=total%len(abc)
                letradesencrip=abc[pos]
                desencrip+=letradesencrip
                aux=1
        if aux==0:
            desencrip+=letra
    return desencrip,clave