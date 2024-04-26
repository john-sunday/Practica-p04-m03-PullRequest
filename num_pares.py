def suma_numeros_pares(inicio, fin):
    suma = 0
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            suma += num
    return suma

# Solicitar al usuario el rango
inicio = int(input("Ingresa el número inicial del rango: "))
fin = int(input("Ingresa el número final del rango: "))

# Calcular la suma de los números pares en el rango dado
resultado = suma_numeros_pares(inicio, fin)

# Mostrar el resultado
print(f"La suma de los números pares en el rango de {inicio} a {fin} es: {resultado}")

