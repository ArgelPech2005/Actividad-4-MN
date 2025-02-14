#   Codigo que implementa el esquema numerico 
#   del metodo de biseccion
# 
"""   Autor:
   Argel Jesus Pech Manrique
   argelpech098@gmail.com
   Version 2.0 : 03/02/2025 01:30am
"""


import numpy as np
import matplotlib.pyplot as plt

# Definir la función que se va a utilizar en el método de bisección
def f(x):
    return np.cos(x) - x #np.exp(-x)-x #x**3 - 4.0*x - 9.0  # Función dada

# Implementación del método de bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    # Verificar si el método es aplicable en el intervalo dado
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    # Listas para almacenar los valores de iteraciones y errores
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cua = []
    c_old = a  # Variable para almacenar el valor anterior de c y calcular errores

    # Imprimir encabezado de la tabla de iteraciones
    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error_abs     |     Error_rel     |     Error_cua     ")
    print("-" * 85)

    # Proceso iterativo del método de bisección
    for i in range(max_iter):
        c = (a + b) / 2  # Calcular el punto medio del intervalo
        iteraciones.append(c)  # Almacenar la iteración actual
        
        # Calcular errores
        error_abs = abs(c - c_old)
        error_rel = error_abs / c
        error_cua = (c - c_old) ** 2
        
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cua.append(error_cua)

        # Imprimir los valores de la iteración actual
        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cua:.8e}")

        # Criterios de parada
        if abs(f(c)) < tol or error_abs < tol:
            break  # Terminar si el error es menor que la tolerancia

        # Determinar el nuevo intervalo para la siguiente iteración
        if f(a) * f(c) < 0:
            b = c  # La raíz está en el intervalo [a, c]
        else:
            a = c  # La raíz está en el intervalo [c, b]
        
        c_old = c  # Actualizar el valor anterior de c

    return iteraciones, errores_abs, errores_rel, errores_cua 

# Definir los parámetros iniciales del intervalo
#a, b = 2, 3  # Intervalo donde se busca la raíz
#a, b = 0, 1  # Otro posible intervalo
a, b = 0, 1  # Otro posible intervalo

# Ejecutar el método de bisección
iteraciones, errores_abs, errores_rel, errores_cua = biseccion(a, b)

# Crear la figura para las gráficas
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Generar valores de x para graficar la función en el intervalo expandido
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

# Primera gráfica: función y convergencia de iteraciones
ax[0].plot(x, y, label=r'$f(x) = cos(x) - x$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)  # Línea en y=0
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Segunda gráfica: convergencia de los errores
ax[1].plot(range(1, len(errores_abs) + 1), errores_abs, label="Error Absoluto", marker='o', linestyle='-', color='r')
ax[1].plot(range(1, len(errores_rel) + 1), errores_rel, label="Error Relativo", marker='s', linestyle='-', color='b')
ax[1].plot(range(1, len(errores_cua) + 1), errores_cua, label="Error Cuadrático", marker='^', linestyle='-', color='y')
ax[1].set_yscale("log")  # Escala logarítmica para visualizar mejor la convergencia
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Errores")
ax[1].set_title("Errores de cada Iteración")
ax[1].legend()
ax[1].grid()

# Guardar la figura en un archivo de imagen
plt.savefig("biseccion_convergencia.png", dpi=300)
plt.show()  # Mostrar las gráficas

