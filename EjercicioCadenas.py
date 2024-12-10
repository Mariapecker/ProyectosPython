'''
Vamos a crear una función que cuente las vocales de un texto y devuelva 
qué vocales aparecen, así emplearemos los métodos de str. vistos y varios bucles if'''

'''
FUNCIÓN:
cuenta_vocales: cuenta las vocales de un texto y devuelve cuáles hay y cuál es la que más se repite

ENTRADA: String en minúsculas y con todos sus caracteres letras

SALIDA: qué vocales aparecen en el texto
'''

def cuenta_vocales(texto):
    #primero vamos a definir error si el texto contiene mayúsculas empleando los métodos str. vistos
    if not str.islower(texto):
        print("para emplear esta función los caracteres deben estar en minúscula, por tanto, convertiremos su texto a minúsculas")
        texto = str.lower(texto)
    #creamos un texto inicial el cual iremos modificando según aparezca cada vocal en el texto
    resultado = "En el texto aparecen las siguientes vocales: "
    if "a" in texto:
        resultado = resultado + "a, "
    if "e" in texto:
        resultado = resultado + "e, "
    if "i" in texto:
        resultado = resultado + "i, "
    if "o" in texto:
        resultado = resultado + "o, "
    if "u" in texto:
        resultado = resultado + "u, "
    #creamos un último if para devolver cuando no hay vocales y empleamos operadores lógicos
    #y en el else quitamos la coma final y ponemos un punto.
    if resultado == "En el texto aparecen las siguientes vocales: ":
        resultado = "En el texto no hay ninguna vocal"
    else:
        resultado = resultado[:-2] + "."

    return resultado

print("prueba 1: " + cuenta_vocales("Estamos todos aqui hoy reunidos"))
print("prueba 2: " + cuenta_vocales("726e82"))
print("prueba 3: " + cuenta_vocales("lkjhgpt"))
      
    
    