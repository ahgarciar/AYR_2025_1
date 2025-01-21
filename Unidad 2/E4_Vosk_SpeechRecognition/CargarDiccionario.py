
def carga():
    archivo = open("../Archivos/Diccionario.txt")
    contenido = archivo.readlines()
    contenido = [i.replace("\n","") for i in contenido]
    #print(contenido)
    return contenido


if __name__ == "__main__":
    dicc = carga()
    print(dicc)
