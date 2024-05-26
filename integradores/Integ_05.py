## TODO 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

### Interativa
def get_int_iterativo():
    while True:
        try:
            valor = int(input("Introduce un número entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Por favor, introduce un número entero.")


### Recursiva
def get_int_recursivo():
    try:
        valor = int(input("Introduce un número entero: "))
        return valor
    except ValueError:
        print("Valor no válido. Por favor, introduce un número entero.")
        return get_int_recursivo()

# # Prueba de funcion
numero = get_int_iterativo()
print(f"Con el metodo iterativo, el número introducido es: {numero}")

numero = get_int_recursivo()
print(f"Con el metodo recursivo, el número introducido es: {numero}")