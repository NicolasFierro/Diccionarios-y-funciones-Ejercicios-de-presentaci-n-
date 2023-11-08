# Ejemplo de función saludar
def saludar():
    print("saludo")

# Ejemplo de función retornarnumero
def retornarnumero():
    return 1

# Llamada a la función saludar
saludar()  # Llama a la función "saludar" que imprime un saludo en la consola

# Llamada a la función retornarnumero
retornarnumero()  # Llama a la función "retornarnumero," pero no hace nada con el valor retornado

# Comprobar el valor devuelto por la función retornarnumero
if retornarnumero() == 1:
    print("Devolvió un uno")  # Comprueba si la función "retornarnumero" devuelve 1 y muestra un mensaje en consecuencia
else:
    print("No devolvió un uno")  # Si la función no devuelve 1, muestra un mensaje diferente

# Función raiz con parámetro
def raiz(value):
    return value ** (1/2)

print(f'La raíz cuadrada es: {raiz(4)}')  # Calcula la raíz cuadrada de 4 y la imprime en la consola

# Función validarsiexiste con parámetro
def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")  # Comprueba si el valor de "obj" es True y muestra un mensaje
    else:
        print(f"{obj} is False")  # Si "obj" no es True, muestra otro mensaje

validarsiexiste(1)  # Llama a la función "validarsiexiste" con el valor 1

# Función que suma cuadrados
def suma_cuadrados(x, y):
    return x ** 2 + y ** 2  # Calcula el cuadrado de x y el cuadrado de y, luego suma los resultados

resultado = suma_cuadrados(3, 5)  # Llama a la función "suma_cuadrados" con los valores 3 y 5
print(f'El resultado es: {resultado}')  # Imprime el resultado en la consola

# Función de compra con parámetros posicionales
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )

print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')  # Calcula el costo de una compra de 3 productos AMD

# Función de compra con parámetros nominales
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )

print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')  # Lo mismo que el ejemplo anterior, pero usando argumentos nominales

# Función de compra con parámetros por defecto
def compra(marca, cantidad, valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )

print(f'Lo comprado fue: {compra("AMD", 3)}')  # Lo mismo que el ejemplo anterior, pero con un valor por defecto para "valor"

# Función que cuenta palabras con función lambda
numero_palabras = lambda t: len(t.strip().split())
print(numero_palabras("Hola, esto es una prueba con lambda"))  # Cuenta las palabras en una cadena usando una función lambda

# Función lambda operadorand
operadorand = lambda x, y: x & y  # Define una función lambda para realizar una operación "AND" entre x e y

for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")  # Aplica la función lambda a diferentes valores de i y j
