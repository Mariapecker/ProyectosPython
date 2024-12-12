#gestión de peliculas
'''
peliculas = {
"Nombre de la Película": {
"director": "Nombre del Director",
"año": Año de Lanzamiento,
"presupuesto": Presupuesto en Millones
}
'''

def anadir_pelicula(peliculas, peli, datos):
    if peli not in peliculas:
        peliculas[peli] = datos
    else:
        print("La película ya está en la lista")

def eliminar_pelicula(peliculas, peli):
    if peli in peliculas:
        del(peliculas[peli])

def mostrar_peliculas(dict):
    if dict == {}:
        print("No hay elementos en la lista de películas.")
    else:
        print("Las películas que se encuentran actualmente en la lista son:")
        for x in dict:
            print(x)
            for y in dict[x]:
                print(y + ":" + dict[x][y])
    
def buscar_pelicula(peliculas, peli):
    if peli in peliculas:
        print("La película " + peli + " sí está en la lista")
    else:
        print("La película 1" + peli + " no está en la lista")

def modificar_pelicula(peliculas, peli, datos):
    if peli in peliculas:
        peliculas[peli] = datos
    else:
        print("La película no está en la lista y por tanto sus datos no se pueden modificar.")

def main():
    peliculas = {}

    while True:
        print("1. Añadir película")
        print("2. Eliminar película")
        print("3. Mostrar películas")
        print("4. Buscar película")
        print("5. Modificar datos de la pelicula")

        elige = input("Selecciona una opción del 1 al 5: ")

        if elige == "1":
            peli = input("Introduce el nombre de la película que quieras añadir a la lista: ")
            director = input("Introduce el director de dicha película: ")
            year = input("Introduce el año de lanzamiento de la película: ")
            p = input("Introduce el presupuesto que tuvo la película en millones: ")
            datos = {"Director" : director, "Año de lanzamiento" : year, "Presupuesto en millones" : p}
            anadir_pelicula(peliculas, peli, datos)
        elif elige == "2":
            peli = input("Introduce el nombre de la película que quieras eliminar de la lista: ")
            eliminar_pelicula(peliculas, peli)
        elif elige == "3":
            mostrar_peliculas(peliculas)
        elif elige == "4":
            peli = input("Introduce el nombre de la película que quieras buscar en la lista: ")
            buscar_pelicula(peliculas, peli)
        elif elige == "5":
            peli = input("Introduce la película que quieras modificar: ")
            director = input("Introduce el director de dicha película: ")
            year = input("Introduce el año de lanzamiento de la película: ")
            p = input("Introduce el presupuesto que tuvo la película en millones: ")
            datos = {"Director" : director, "Año de lanzamiento" : year, "Presupuesto en millones" : p}
            modificar_pelicula(peliculas, peli, datos)
        else:
            print("Opción no válida, por favor introduzca un número entre el 1 y el 5.")

if __name__ == "__main__":
    main()