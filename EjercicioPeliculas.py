#gestión de peliculas

def anadir_pelicula(peliculas, peli):
    if peli not in peliculas:
        peliculas = peliculas.append(peli)

def eliminar_pelicula(peliculas, peli):
    if peli in peliculas:
        peliculas.remove(peli)

def mostrar_peliculas(lista):
    print("Las películas que se encuentran actualmente en la lista son:")
    for i in range(len(lista)):
        print(lista[i])
    
def buscar_pelicula(peliculas, peli):
    if peli in peliculas:
        print("La película " + peli + " sí está en la lista")
    else:
        print("La película 1" + peli + " no está en la lista")

def main():
    peliculas = []

    while True:
        print("1. Añadir película")
        print("2. Eliminar película")
        print("3. Mostrar películas")
        print("4. Buscar película")

        elige = input("Selecciona una opción del 1 al 4: ")

        if elige == "1":
            peli = input("Introduce el nombre de la película que quieras añadir a la lista: ")
            anadir_pelicula(peliculas, peli)
        elif elige == "2":
            peli = input("Introduce el nombre de la película que quieras eliminar de la lista: ")
            eliminar_pelicula(peliculas, peli)
        elif elige == "3":
            mostrar_peliculas(peliculas)
        elif elige == "4":
            peli = input("Introduce el nombre de la película que quieras buscar en la lista: ")
            buscar_pelicula(peliculas, peli)
        else:
            print("Opción no válida, por favor introduzca un número entre el 1 y el 4.")

if __name__ == "__main__":
    main()