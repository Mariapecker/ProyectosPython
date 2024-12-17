#prueba de series y operaciones aritméticas
import pandas as pd

#creamos una serie
s = pd.Series([1, 2, 3, 4, 5, 6])

#mostramos la serie
print(s)

#añadimos un elemento
nuevo_elem = pd.Series([7])

s = s.add(nuevo_elem)

print(s)

#eliminamos un elemento
s = s.drop([2])

print(s)

#aplicamos a nuestra serie s las operaciones básicas
suma = s + s
print("Suma: " + suma)

resta = s - s
print("Resta: " + resta)

prod = s * s
print("Multiplicación: " + prod)

div = s / s
print("División: " + div)