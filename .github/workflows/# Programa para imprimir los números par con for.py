# Programa para imprimir los números pares del 1 al 20 usando for

# Usamos for porque conocemos el rango de valores que vamos a recorrer (1 a 20).

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)
