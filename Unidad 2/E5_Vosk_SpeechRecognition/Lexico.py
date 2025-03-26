import CargarDiccionario as modulo_carga

def validar_cadena(cad): #limpiar cadena
    dicc_completo = modulo_carga.carga()  # cargar diccionario

    dicc = []
    for palabra in dicc_completo:
        if not "-" in palabra and not palabra=="":
            dicc.append(palabra)

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
    #***

    valida = True
    comando = cadena.split(" ")

    for token in comando:
        valida = token in dicc
        if not valida:
            break
          
    return valida

    #NOTA... un comando por oracion!

if __name__ =="__main__":
    c = "Mover Derecha"
    resultado = validar_cadena(c)
    print(resultado)