texto_largo = ["Línea" + str(i+1)for i in range(1000)]
#print(texto_largo)
def dividir_texto(texto):
    lista = []
    for i in range(40):
        lista.append(texto[:25])
        texto = texto[25:]
    return lista

print(dividir_texto(texto_largo))

