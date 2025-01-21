import CargarDiccionario as c

def procesar_cadena(cad): #limpiar cadena
    dicc = c.carga()  # cargar diccionario

    cadena = cad
    # mayusculas y minisculas -> homologar de acuerdo con el diccionario
    cadena = cadena.lower() #pasa a minusculas # COMPLETO! _:D!

    # algunas palabras van a tener acentos y otras no....-> quitar acentos
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")

    # sin simbolos de admiracion, iterrogacion, comas
    cadena = cadena.replace(",", "")
    cadena = cadena.replace("!", "")
    cadena = cadena.replace("¡", "")
    cadena = cadena.replace("?", "")
    cadena = cadena.replace("¿", "")

    # word2number <--- convertir cadenas a numeros..
    #PENDIENTE

    # convertir a lista cada palabra ... separada por espacio
    comando = cadena.split(" ")

    # eliminar palabras que no esten en el diccionario   #type
    for idx in range(len(comando), 0, -1):
        if not comando[idx] in dicc:
            del comando[idx]

    return comando







    #NOTA... un comando por oracion!

if __name__ =="__main__":
    c = "Prende el foco de la cocina"
    resultado = procesar_cadena(c)
    print(resultado)