#importamos pandas para poder trabajar con series
import pandas as pd

#primero hacemos las listas con los datos que nos piden
#datosA contiene datos de temperaturas en grados celsius de una ciudad
datosA = [20.0, 17.8, 13.5, 10.4, 9.8, 7.5]

#datosB contiene los datos de lluvias en esa misma ciudad en milímetros
datosB = [0.0, 0.5, 1.8, 2.1, 2.2, 2.7]

#hacemos series a partir de nuestras listas de datos

serieA = pd.Series(datosA)

serieB = pd.Series(datosB)

#hacemos un slicing en ambas series, por ejemplo para fijarnos en los días más fríos y lluviosos

sub_serieA = serieA[2:5]

sub_serieB = serieB[2:5]

#concatenamos ambas subseries

serie_concatenada = pd.concat([sub_serieA, sub_serieB], ignore_index=True)

print(serie_concatenada)

#finalmente realizamos algunas operaciones básicas a nuestra nueva serie

suma = serie_concatenada + serieB

div = serie_concatenada / serieA

print(suma)

print(div)