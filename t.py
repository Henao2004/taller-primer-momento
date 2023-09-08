print("=== Festival de Música ===")
print("1. Registrar agrupación musical")
print("2. Mostrar bandas no presentadas")
print("3. Cambiar hora de presentación")
print("4. Retirar agrupación no presentada")
print("5. Ver todas las bandas registradas")
print("0. Salir")

agrupaciones = []  # Inicializar una lista vacía para almacenar información sobre las agrupaciones musicales registradas

while True:  # Iniciar un bucle infinito que permite que el programa se ejecute continuamente
    opcion = int(input("Seleccione una opción: "))  # Solicitar al usuario que seleccione una opción del menú y almacenarla en la variable 'opcion'

    if opcion == 1:  # Si la opción seleccionada es 1, registrar una nueva agrupación musical
        agrupacion = {}  # Inicializar un diccionario para almacenar los detalles de la agrupación
        agrupacion["nombre"] = input("Nombre de la agrupación: ")  # Solicitar el nombre de la agrupación y almacenarlo en el diccionario
        agrupacion["id"] = int(input("Ingrese el ID de la agrupación: "))  # Solicitar el ID de la agrupación y almacenarlo en el diccionario
        agrupacion["genero"] = input("Género musical: ")  # Solicitar el género musical y almacenarlo en el diccionario
        agrupacion["hora_presentacion"] = input("Hora de presentación (HH:MM): ")  # Solicitar la hora de presentación y almacenarla en el diccionario
        agrupacion["pago"] = float(input("Pago a la agrupación: "))  # Solicitar el pago y almacenarlo en el diccionario
        estado = input("¿La agrupación ya se presentó? (True/False): ").lower()  # Solicitar si la agrupación ya se presentó y convertir la entrada a minúsculas
        agrupacion["estado"] = estado == 'true'  # Convierte la entrada a un valor booleano y almacena el estado en el diccionario
        agrupaciones.append(agrupacion)  # Agregar el diccionario de agrupación a la lista de agrupaciones
        print(f"{agrupacion['nombre']} ha sido registrado.")  # Mostrar un mensaje de confirmación

    elif opcion == 2:  # Si la opción seleccionada es 2, mostrar las bandas no presentadas
        print("Agrupaciones no presentadas:")
        for agrupacion in agrupaciones:  # Iterar a través de la lista de agrupaciones
            if not agrupacion["estado"]:  # Verificar si la agrupación no se ha presentado (estado es False)
                print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Hora de presentación: {agrupacion['hora_presentacion']}")

    elif opcion == 3:  # Si la opción seleccionada es 3, cambiar la hora de presentación
        id_a_cambiar = int(input("Ingrese el ID de la agrupación a la que desea cambiar la hora: "))  # Solicitar el ID de la agrupación a modificar
        for agrupacion in agrupaciones:  # Iterar a través de la lista de agrupaciones
            if agrupacion["id"] == id_a_cambiar:  # Si se encuentra una agrupación con el ID ingresado
                while True:  # Iniciar un bucle para asegurarse de que se ingrese una hora válida
                    nueva_hora = input(f"Ingrese la nueva hora de presentación para {agrupacion['nombre']} (HH:MM): ")  # Solicitar la nueva hora
                    # Verificar si la entrada es una hora válida en formato "HH:MM"
                    if len(nueva_hora) == 5 and nueva_hora[2] == ':' and nueva_hora[:2].isdigit() and nueva_hora[3:].isdigit():
                        agrupacion["hora_presentacion"] = nueva_hora  # Actualizar la hora de presentación en el diccionario
                        print(f"Hora de presentación actualizada para {agrupacion['nombre']}.")
                        break 
                              # Salir del bucle de verificación de hora
                    else:
                        print("Hora inválida. Ingrese la hora en formato HH:MM.")  # Mostrar un mensaje de error si la hora no es válida
                break  # Salir del bucle de búsqueda de agrupaciones una vez que se actualiza la hora

    elif opcion == 4:  # Si la opción seleccionada es 4, retirar una agrupación no presentada
        id_a_retirar = int(input("Ingrese el ID de la agrupación que desea retirar: "))  # Solicitar el ID de la agrupación a retirar
        for agrupacion in agrupaciones:  # Iterar a través de la lista de agrupaciones
            if agrupacion["id"] == id_a_retirar and not agrupacion["estado"]:  # Verificar si se encuentra una agrupación con el ID ingresado que no se ha presentado
                agrupaciones.remove(agrupacion)  # Eliminar la agrupación de la lista de agrupaciones
                print(f"{agrupacion['nombre']} ha sido retirado del listado de agrupaciones.")  # Mostrar un mensaje de confirmación
                break  # Salir del bucle de búsqueda de agrupaciones

    elif opcion == 5:  # Si la opción seleccionada es 5, mostrar todas las bandas registradas
        print("Todas las bandas registradas:")
        for agrupacion in agrupaciones:  # Iterar a través de la lista de agrupaciones
            print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Género: {agrupacion['genero']}, Hora de presentación: {agrupacion['hora_presentacion']}, Pago: ${agrupacion['pago']}, ¿Ya se presentó? {agrupacion['estado']}")

    elif opcion == 0:  # Si la opción seleccionada es 0, salir del programa
        print("Saliendo del programa.")
        break  # Salir del bucle principal y finalizar el programa

    else:  # Si se selecciona una opción no válida (fuera del rango 0-5), mostrar un mensaje de error
        print("Opción inválida. Por favor, seleccione una opción válida.")
