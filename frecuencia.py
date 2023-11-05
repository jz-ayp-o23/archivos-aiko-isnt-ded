def frecuencia_palabras_en_archivo(archivo_entrada, archivo_salida):
    """
    Analiza la frecuencia con la que aparecen palabras en un archivo
    """
    frecuencias = {} #Crea un diccionario
    with open(archivo_entrada, "r", encoding="utf8") as f:
        #Leer cada línea
        for linea in f:
            #Dejar únicamente letras y espacios
            linea = linea.lower() 
            letras = ""
            for caracter in linea:
                if caracter.isalpha() or caracter == " ":
                    letras += caracter
            palabras = letras.split() #Separa las palabras en una lista
            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
                else:
                    frecuencias[palabra] = 1
    
    #Ordenar el diccionario por frecuencia
    #La colección .items() de un diccionario son las tuplas (clave, valor) que lo conforman
    items = frecuencias.items()
    #sorted + reverse = True, 
    #lambda crea una función anónima, es decir, sin nombre
    #"lambda item: item[1]" quiere decir:
    #def nombre(item):
    #   return item[1]
    items = sorted(items, key=lambda item: item[1], reverse= True)
    #Convertir las tuplas ordenadas en diccionario
    frecuencias = dict(items)

    #Escribir el archivo de salida
    with open(archivo_salida, "w", encoding="utf8") as f:
        for palabra in frecuencias:
            linea = f"{palabra}: {frecuencias[palabra]} \n"
            f.write(linea)
    #Regresar el diccionario
    return frecuencias

def main():
    """Probar la función"""
    archivo = "data/Asimov, Isaac - Cómo ocurrió.txt"
    salida = "data/Asimov-análisis.txt"
    prueba = frecuencia_palabras_en_archivo(archivo, salida)
    #Mostrar las 10 palabras más frecuentes
    i = 0
    for palabra in prueba:
        print(f"{palabra}: {prueba[palabra]}")
        i += 1
        if i >= 10:
            break
    return

main()