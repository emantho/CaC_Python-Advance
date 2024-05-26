## TODO 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con "la palabra" más repetida y su frecuencia.

from Integ_03 import contar_palabras

def palabra_mas_repetida(frecuencias):
    
    palabra_max = None
    max_frecuencia = 0
    
    # Recorrer el diccionario de frecuencias
    for palabra, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            palabra_max = palabra
            max_frecuencia = frecuencia
    
    # Devolver la palabra más repetida y su frecuencia como una tupla
    return (palabra_max, max_frecuencia)

# Ejemplo de uso con el diccionario generado anteriormente
frecuencias = contar_palabras("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here',")
resultado = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: {resultado}")