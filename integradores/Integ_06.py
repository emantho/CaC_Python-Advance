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

# # Prueba de funcion
# try:
#     persona = Persona("Juan", 25, "12345678A")
#     persona.mostrar()
#     print("Mayor de edad:", persona.es_mayor_de_edad())

#     # Probar validación de nombre
#     persona.nombre = "Mario"
#     print("Nombre actualizado:", persona.nombre)
    
#     # Probar validación de edad
#     persona.edad = 30
#     print("Edad actualizada:", persona.edad)

#     # Probar validación de dni
#     persona.dni = 87654321
#     print("DNI actualizado:", persona.dni)

# except ValueError as e:
#     print(e)