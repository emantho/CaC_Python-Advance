## TODO 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
import string

def contar_palabras(cadena):
    # normalizando texto
    cadena = cadena.lower()
    
    # Eliminando signos de puntuación y diviendo el texto
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
    
    palabras = cadena.split()
    
    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

# # Prueba de funcion
cadena = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here',"
resultado = contar_palabras(cadena)
print(resultado)