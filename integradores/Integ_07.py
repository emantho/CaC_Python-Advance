## TODO 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
    # Un constructor, donde los datos pueden estar vacíos.
    # Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    # mostrar(): Muestra los datos de la cuenta.
    # ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    # retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

# Para validar el titular se llama la clase Persona de ejercicio #6
from Integ_06 import Persona

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

# # Prueba de funcion
# try:
#     titular = Persona("Juan", 25, "12345678A")
#     cuenta = Cuenta(titular)

#     # Mostrar datos de la cuenta
#     cuenta.mostrar()

#     # Ingresar dinero
#     cuenta.ingresar(1000.50)
#     cuenta.mostrar()

#     # Retirar dinero
#     cuenta.retirar(300.75)
#     cuenta.mostrar()

#     # Intentar ingresar una cantidad negativa
#     cuenta.ingresar(-500)
#     cuenta.mostrar()

#     # Retirar más de lo que hay en la cuenta
#     cuenta.retirar(800)
#     cuenta.mostrar()

# except ValueError as e:
#     print(e)