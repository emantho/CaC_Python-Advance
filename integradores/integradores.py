# Ejercicios integradores para revisar en la clase 7

## TODO 1 Escribir una función que calcule el máximo común divisor entre dos números.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
print()
print("-------------------------------")
print()
## TODO 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
num1 = 180
num2 = 324
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")
print()
print("-------------------------------")
print()
## TODO 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def contar_palabras(cadena):
    # Convertir la cadena a minúsculas para que la cuenta no sea sensible a mayúsculas/minúsculas
    cadena = cadena.lower()
    
    # Eliminar signos de puntuación
    import string
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
    
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Crear un diccionario para almacenar las frecuencias de las palabras
    frecuencias = {}
    
    # Contar las frecuencias de las palabras
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

# Ejemplo de uso
cadena = "Hola mundo! Hola a todos en el mundo. Mundo, mundo, mundo!"
resultado = contar_palabras(cadena)
print(resultado)
print()
print("-------------------------------")
print()
## TODO 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def palabra_mas_repetida(frecuencias):
    # Inicializar variables para almacenar la palabra más repetida y su frecuencia
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
frecuencias = contar_palabras("Hola mundo! Hola a todos en el mundo. Mundo, mundo, mundo!")
resultado = palabra_mas_repetida(frecuencias)
print(resultado)
print()
print("-------------------------------")
print()
## TODO 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

### Interativa
def get_int_iterativo():
    while True:
        try:
            valor = int(input("Introduce un número entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Por favor, introduce un número entero.")

# Ejemplo de uso
numero = get_int_iterativo()
print(f"El número introducido es: {numero}")

### Recursiva
def get_int_recursivo():
    try:
        valor = int(input("Introduce un número entero: "))
        return valor
    except ValueError:
        print("Valor no válido. Por favor, introduce un número entero.")
        return get_int_recursivo()

# Ejemplo de uso
numero = get_int_recursivo()
print(f"El número introducido es: {numero}")


print()
print("-------------------------------")
print()
## TODO 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
    # Un constructor, donde los datos pueden estar vacíos.
    # Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    # mostrar(): Muestra los datos de la persona.
    # Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Getters y Setters con validación
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 120:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120.")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and dni.strip():
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de caracteres no vacía.")

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    # Método para comprobar si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo de uso
try:
    persona = Persona("Juan", 25, "12345678A")
    persona.mostrar()
    print("Mayor de edad:", persona.es_mayor_de_edad())

    # Probar validación de nombre
    persona.nombre = "María"
    print("Nombre actualizado:", persona.nombre)
    
    # Probar validación de edad
    persona.edad = 30
    print("Edad actualizada:", persona.edad)

    # Probar validación de dni
    persona.dni = "87654321B"
    print("DNI actualizado:", persona.dni)

except ValueError as e:
    print(e)

print()
print("-------------------------------")
print()
## TODO 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
    # Un constructor, donde los datos pueden estar vacíos.
    # Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    # mostrar(): Muestra los datos de la cuenta.
    # ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    # retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 120:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120.")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and dni.strip():
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de caracteres no vacía.")

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona.")
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @property
    def cantidad(self):
        return self._cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad

# Ejemplo de uso
try:
    titular = Persona("Juan", 25, "12345678A")
    cuenta = Cuenta(titular)

    # Mostrar datos de la cuenta
    cuenta.mostrar()

    # Ingresar dinero
    cuenta.ingresar(1000.50)
    cuenta.mostrar()

    # Retirar dinero
    cuenta.retirar(300.75)
    cuenta.mostrar()

    # Intentar ingresar una cantidad negativa
    cuenta.ingresar(-500)
    cuenta.mostrar()

    # Retirar más de lo que hay en la cuenta
    cuenta.retirar(800)
    cuenta.mostrar()

except ValueError as e:
    print(e)

print()
print("-------------------------------")
print()
## TODO 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
    # Un constructor.
    # Los setters y getters para el nuevo atributo.
    # En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    # Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
    # El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    # Getter y Setter para bonificación
    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and 0 <= bonificacion <= 100:
            self._bonificacion = bonificacion
        else:
            raise ValueError("La bonificación debe ser un número entre 0 y 100.")

    # Método para comprobar si el titular es válido
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    # Sobreescribir el método retirar para verificar si el titular es válido
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero de la Cuenta Joven.")

    # Sobreescribir el método mostrar
    def mostrar(self):
        print("Cuenta Joven")
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad: {self.cantidad:.2f}")
        print(f"Bonificación: {self.bonificacion:.2f}%")

# Ejemplo de uso
try:
    titular_joven = Persona("Ana", 20, "98765432C")
    cuenta_joven = CuentaJoven(titular_joven, 1000.0, 10.0)

    # Mostrar datos de la cuenta joven
    cuenta_joven.mostrar()

    # Ingresar dinero
    cuenta_joven.ingresar(500.0)
    cuenta_joven.mostrar()

    # Retirar dinero (válido)
    cuenta_joven.retirar(200.0)
    cuenta_joven.mostrar()

    # Intentar retirar más dinero siendo titular inválido (mayor de 25)
    titular_no_valido = Persona("Carlos", 30, "12345678B")
    cuenta_no_valida = CuentaJoven(titular_no_valido, 1000.0, 10.0)
    cuenta_no_valida.retirar(100.0)
    cuenta_no_valida.mostrar()

except ValueError as e:
    print(e)
