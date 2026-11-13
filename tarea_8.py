import funciones_8 as f
import os

def mostrar_menu():
    print("\n===== GESTIÓN DE CANCIONES =====")
    print("1. Agregar canción")
    print("2. Ver canciones")
    print("3. Eliminar canción")
    print("4. Buscar canción")
    print("5. Salir")


def main():
    canciones = [
        {"titulo": "Halo", "artista": "pedrito"},
        {"titulo": "Fallout", "artista": "juanito"}
    ]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system("cls" if os.name == "nt" else "clear")
            titulo = input("Ingrese el título de la canción: ")
            artista = input("Ingrese el artista: ")
            print(f.agregar_cancion(canciones, titulo, artista))

        elif opcion == "2":
            os.system("cls" if os.name == "nt" else "clear")
            f.ver_canciones(canciones)

        elif opcion == "3":
            os.system("cls" if os.name == "nt" else "clear")
            titulo = input("Ingrese el título de la canción a eliminar: ")
            print(f.eliminar_cancion(canciones, titulo))

        elif opcion == "4":
            os.system("cls" if os.name == "nt" else "clear")
            texto = input("Ingrese el título o artista a buscar: ")
            resultado = f.buscar_cancion(canciones, texto)
            if resultado:
                print(resultado)

        elif opcion == "5":
            print("Gracias por usar el programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()