# Declaración de un diccionario vacío
mi_diccionario = dict()  # Creación de un diccionario vacío utilizando la función dict()
mi_diccionario = {}  # Creación de un diccionario vacío utilizando llaves

# Diccionario inicializado con valores
Datos = {'ciudad': 'Nueva York', 'poblacion': 8500000}

# Accediendo a los elementos de un diccionario
print(Datos['ciudad'])  # Imprimir la ciudad
print(Datos.get('poblacion', 'No disponible'))  # Imprimir la población o 'No disponible' si no está presente

# Agregar datos al diccionario después de creado
nuevos_datos = {'temperatura': 25, 'idioma': 'inglés'}
Datos.update(nuevos_datos)  # Actualizar el diccionario 'Datos' con nuevos datos

# Técnicas de iteración en diccionarios
calificaciones = {
    'Juan': 4.5,
    'Maria': 3.8,
    'Luis': 4.0,
    'Ana': 3.2
}

# Iterar por clave y valor
for nombre, calificacion in calificaciones.items():
    print(nombre, calificacion)

# Iterar por clave
print("Técnicas por clave")
for nombre in calificaciones.keys():
    print(nombre)

# Iterar por valor
print("Iterar por valor")
for calificacion in calificaciones.values():
    print(calificacion)

# Operaciones sobre los diccionarios
cuadrados = {num: num**2 for num in (2, 3, 5, 7)}  # Crear un nuevo diccionario con números al cuadrado
print(cuadrados)

# Imprimir números en reversa
print("Números en reversa")
for i in reversed(range(1, 11, 2)):
    print(i)

# Borrar un elemento del diccionario
del calificaciones['Maria']  # Eliminar la clave 'Maria' del diccionario 'calificaciones'
for nombre, calificacion in calificaciones.items():
    print(nombre, calificacion)
