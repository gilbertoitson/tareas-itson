estudiantes = []


def mostrar_menu():
    print("\n--- Sistema de registro de estudiantes ---")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes registrados")
    print("3. Consultar el promedio de un estudiante")
    print("4. Mostrar estadísticas generales del grupo")
    print("5. Salir del programa")


def calcular_promedio(calificaciones):
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion
    return suma / len(calificaciones)


def registrar_estudiante():
    while True:
        identificacion = input("Número de identificación: ").strip()
        if identificacion == "":
            print("La identificación no puede quedar vacía.")
            continue

        estudiante_repetido = False
        for estudiante in estudiantes:
            if identificacion == estudiante["identificacion"]:
                estudiante_repetido = True
                break
        if not estudiante_repetido:
            break
        print("Ya existe un estudiante con esa identificación.")

    nombre = input("Nombre: ").strip()
    while nombre == "":
        print("El nombre no puede quedar vacío.")
        nombre = input("Nombre: ").strip()

    calificaciones = []
    for numero in range(1, 4):
        while True:
            try:
                calificacion = float(input("Calificación {} (0-100): ".format(numero)))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Ingresa un número válido.")

    calificaciones = tuple(calificaciones)
    promedio = calcular_promedio(calificaciones)
    aprobado = promedio >= 70
    situacion = "Aprobado" if aprobado else "Reprobado"

    estudiantes.append({
        "identificacion": identificacion,
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "aprobado": aprobado,
        "situacion": situacion
    })
    print("Estudiante registrado correctamente.")


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("Todavía no hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print("\nIdentificación: {}".format(estudiante["identificacion"]))
        print("Nombre: {}".format(estudiante["nombre"]))
        print("Calificaciones: {}".format(estudiante["calificaciones"]))
        print("Promedio: {:.2f}".format(estudiante["promedio"]))
        print("Situación académica: {}".format(estudiante["situacion"]))


def consultar_estudiante():
    identificacion = input("Identificación del estudiante: ").strip()
    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            print("Nombre: {}".format(estudiante["nombre"]))
            print("Promedio: {:.2f}".format(estudiante["promedio"]))
            print("Situación académica: {}".format(estudiante["situacion"]))
            return
    print("No se encontró un estudiante con esa identificación.")


def mostrar_estadisticas():
    if len(estudiantes) == 0:
        print("Todavía no hay estudiantes registrados.")
        return

    suma_promedios = 0
    aprobados = 0
    reprobados = 0
    promedio_mas_alto = estudiantes[0]["promedio"]

    for estudiante in estudiantes:
        suma_promedios += estudiante["promedio"]
        if estudiante["aprobado"]:
            aprobados += 1
        else:
            reprobados += 1
        if estudiante["promedio"] > promedio_mas_alto:
            promedio_mas_alto = estudiante["promedio"]

    promedio_general = suma_promedios / len(estudiantes)
    print("\n--- Estadísticas generales ---")
    print("Estudiantes registrados: {}".format(len(estudiantes)))
    print("Promedio general: {:.2f}".format(promedio_general))
    print("Aprobados: {}".format(aprobados))
    print("Reprobados: {}".format(reprobados))
    print("Promedio más alto: {:.2f}".format(promedio_mas_alto))


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            consultar_estudiante()
        elif opcion == "4":
            mostrar_estadisticas()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inexistente. Intenta de nuevo.")


if __name__ == "__main__":
    main()