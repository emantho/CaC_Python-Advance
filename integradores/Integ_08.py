## TODO 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
    # Un constructor.
    # Los setters y getters para el nuevo atributo.
    # En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    # Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
    # El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

# Importando titular y cuenta de ejercicios #6 y #7
from Integ_06 import Persona
from Integ_07 import Cuenta

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
