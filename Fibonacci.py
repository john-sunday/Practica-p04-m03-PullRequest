# SUCESIÓN DE FIBONACCI
# Es una serie infinita de números naturales que mantiene el '0' y '1' como primeros 
# dígitos el tercer digito y los siguientes, son la suma de los dos anteriores...

def serie_fibcc(m):
    seq_fibcc = [0, 1]
    while len(seq_fibcc) < m:
        seq_fibcc.append(seq_fibcc[-1] + seq_fibcc[-2])
    return seq_fibcc[:m]

# --- LO PROBAMOS---
m = 6; serie = serie_fibcc(m)
print(f"La Serie fibonacci para un valor de {m} es {serie}")

# m - longitud de la secuencia de la serie

# En este codigo se comienza con una lista con elementos '0' y '1'
# y despues con un bucle while se añade el resto de la secuencia
# hasta el valor m.
# ////////////////////////////////////////////////////////////////
# Este codigo devuelve como salida una lista con '6' elementos:
# [0, 1, 1, 2, 3, 5]
