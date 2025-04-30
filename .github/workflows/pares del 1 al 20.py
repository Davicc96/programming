
# Programa para imprimir los números pares del 1 al 20 usando while

# Inicializamos el contador
numero: int = 1

# Usamos while porque no sabemos de antemano cuántas veces se iterará exactamente.
# La condición es simple y clara para este caso.

while numero <= 20:
    # Comprobamos si el número es par
    if numero % 2 == 0:
        print(numero)
    numero += 1  # Incrementamos el número
