import numpy as np
from pathlib import Path

def promedios(entrada):
    archivo = Path(entrada) #Obtiene el path de la entrada 
    salida = str(archivo.with_name("promedios" + archivo.suffix)) #Define el path de la salida
    with open(archivo, "r", encoding="utf8") as f_in: #Abre la entrada
        with open(salida, "w", encoding="utf8") as f_out: #Abre la salida para escribir
            for linea in f_in: #Separa las líneas de la entrada
                alumno = linea.split() 
                nombre = alumno[0]
                apellido = alumno[1].upper()
                calificaciones = alumno[2:]
                promedio = sum(np.float_(calificaciones))/len(calificaciones) #Calcula el promedio
                f_out.write(f"{apellido}, {nombre}: {promedio:.1f} \n") #Escribe en el archivo de salida
    return

promedios("data/calificaciones.txt")