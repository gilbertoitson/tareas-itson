import os

def agregar_cancion(canciones, titulo, artista):
    """Agrega una canción a la lista."""
    titulo = titulo.strip()
    artista = artista.strip()

    if titulo == "" or artista == "":
        return "Error: el título y el artista no pueden estar vacíos."

    cancion = {
        "titulo": titulo,
        "artista": artista
    }

    canciones.append(cancion)
    return f"Se agregó correctamente: {titulo} - {artista}"


def ver_canciones(canciones):
    """Muestra todas las canciones guardadas."""
    if len(canciones) == 0:
        print("No hay canciones registradas.")
        return

    print("\nLista de canciones:")
    for i, cancion in enumerate(canciones, start=1):
        print(f"{i}. {cancion['titulo']} - {cancion['artista']}")


def eliminar_cancion(canciones, titulo):
    """Elimina una canción por su título."""
    titulo = titulo.strip()

    for i, cancion in enumerate(canciones):
        if cancion["titulo"].lower() == titulo.lower():
            canciones.pop(i)
            return f"Se eliminó la canción: {titulo}"

    return "No se encontró la canción."


def buscar_cancion(canciones, texto):
    """Busca canciones por título o artista."""
    texto = texto.strip().lower()
    resultados = []

    for cancion in canciones:
        if texto in cancion["titulo"].lower() or texto in cancion["artista"].lower():
            resultados.append(cancion)

    if len(resultados) == 0:
        return "No se encontraron coincidencias."

    print("\nResultados de la búsqueda:")
    for i, cancion in enumerate(resultados, start=1):
        print(f"{i}. {cancion['titulo']} - {cancion['artista']}")

    return ""


def menu():
    """Muestra el menú principal."""
    print("\n===== GESTIÓN DE CANCIONES =====")
    print("1. Agregar canción")
    print("2. Ver canciones")
    print("3. Eliminar canción")
    print("4. Buscar canción")
    print("5. Salir")


def main():
    canciones = []

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            os.system("cls" if os.name == "nt" else "clear")
            titulo = input("Ingrese el título de la canción: ")
            artista = input("Ingrese el nombre del artista: ")
            print(agregar_cancion(canciones, titulo, artista))

        elif opcion == "2":
            os.system("cls" if os.name == "nt" else "clear")
            ver_canciones(canciones)

        elif opcion == "3":
            os.system("cls" if os.name == "nt" else "clear")
            titulo = input("Ingrese el título de la canción a eliminar: ")
            print(eliminar_cancion(canciones, titulo))

        elif opcion == "4":
            os.system("cls" if os.name == "nt" else "clear")
            texto = input("Ingrese el título o artista a buscar: ")
            buscar_cancion(canciones, texto)

        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida. Intenta otra vez.")

        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()