peliculas = []
def menu():
    print("1. Añadir película")
    print("2. Eliminar película")
    print("3. Mostrar películas")
    print("4. Buscar película")

def anadir_pelicula(peli):
    if peli not in peliculas:
        peliculas = peliculas.append(peli)

def eliminar_pelicula(peli):
    if peli in peliculas:
        peliculas.remove(peli)

def mostrar_peliculas(lista):
    print("Las películas que se encuentran actualmente en la lista son:")
    for i in range(len(lista)):
        print(lista[i])
    
def buscar_pelicula(peli):
    if peli in peliculas:
        print("La película" + peli + "sí está en la lista")
    else:
        print("La película" + peli + "no está en la lista")

print(menu())