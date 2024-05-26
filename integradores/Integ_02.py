## TODO 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

# Llamando función
num1 = 180
num2 = 324
result = mcm(num1, num2)
print(f"El mcm de {num1} y {num2} es {result}")