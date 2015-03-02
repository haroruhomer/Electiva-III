__author__ = 'haroldhomero'

def Cargar():
    archivo=open("alfabeto.txt", 'r',-1,"utf8")
    lista=[]
    linea=archivo.readline()
    while linea != "":
        if linea!='\n':
            if linea =='\ufeff \n':
                linea=' '
            lista.append(linea)
        linea=archivo.read(1)
    return lista

