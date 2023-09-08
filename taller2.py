print("=== Festival de Música ===")
print("1. Registrar agrupación musical")
print("2. Mostrar bandas no presentadas")
print("3. Cambiar hora de presentación")
print("4. Retirar agrupación no presentada")
print("5. Ver todas las bandas registradas")
print("0. Salir")

agrupaciones = []

while True:
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agrupacion = {}
        agrupacion["nombre"] = input("Nombre de la agrupación: ")
        agrupacion["id"] = int(input("Ingrese el ID de la agrupación: "))
        agrupacion["genero"] = input("Género musical: ")
        agrupacion["hora_presentacion"] = input("Hora de presentación (HH:MM): ")
        agrupacion["pago"] = float(input("Pago a la agrupación: "))
        estado = input("¿La agrupación ya se presentó? (True/False): ").lower()
        agrupacion["estado"] = estado == 'true' 
        # Convierte la entrada a un valor booleano
        agrupaciones.append(agrupacion)
        print(f"{agrupacion['nombre']} ha sido registrado.")

    elif opcion == 2:
        print("Agrupaciones no presentadas:")
        for agrupacion in agrupaciones:
            if not agrupacion["estado"]:
                print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Hora de presentación: {agrupacion['hora_presentacion']}")

    elif opcion == 3:
        id_a_cambiar = int(input("Ingrese el ID de la agrupación a la que desea cambiar la hora: "))
        agrupacion_encontrada = False 
        # Variable para verificar si se encontró la agrupación

        for agrupacion in agrupaciones:
            if agrupacion["id"] == id_a_cambiar and not agrupacion["estado"]:
                agrupacion_encontrada = True
                while True:
                    nueva_hora = input(f"Ingrese la nueva hora de presentación para {agrupacion['nombre']} (HH:MM): ")
                    # Verificar si la entrada es una hora válida en formato "HH:MM"
                    if len(nueva_hora) == 5 and nueva_hora[2] == ':' and nueva_hora[:2].isdigit() and nueva_hora[3:].isdigit():
                        agrupacion["hora_presentacion"] = nueva_hora
                        print(f"Hora de presentación actualizada para {agrupacion['nombre']}.")
                        break
                    else:
                        print("Hora inválida. Ingrese la hora en formato HH:MM.")

        if not agrupacion_encontrada:
            print("No se encontró una agrupación con el ID especificado o la agrupación ya se presentó.")

    elif opcion == 4:
        id_a_retirar = int(input("Ingrese el ID de la agrupación que desea retirar: "))
        for agrupacion in agrupaciones:
            if agrupacion["id"] == id_a_retirar and not agrupacion["estado"]:
                agrupaciones.remove(agrupacion)
                print(f"{agrupacion['nombre']} ha sido retirado del listado de agrupaciones.")
                break
        else:
            print("La opción es inválida (la banda ya se presentó o el ID no existe).")

    elif opcion == 5:
        print("Todas las bandas registradas:")
        for agrupacion in agrupaciones:
            print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Género: {agrupacion['genero']}, Hora de presentación: {agrupacion['hora_presentacion']}, Pago: ${agrupacion['pago']}, ¿Ya se presentó? {agrupacion['estado']}")

    elif opcion == 0:
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        
#DAVID TORO MONTOYA
#Tomas Henao Arroyave
