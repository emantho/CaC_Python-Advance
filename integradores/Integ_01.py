
## TODO 1 Escribir una función que calcule el máximo común divisor entre dos números.
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# calling function
num1 = 48
num2 = 18
result = mcd(num1, num2)
print(f"El mcd de {num1} y {num2} es {result}")