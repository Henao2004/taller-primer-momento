print("****LA SAPICON EL CHOCHO****")
print(" ************************** ")

n = int(input("Ingrese la cantidad de frutas para el salpicón: "))

frutas = []

for i in range(n):
    fruta = {}
    
    fruta["id"] = int(input("Ingrese el Id de la Fruta"))
    fruta["nombre"] = input(f"Nombre de la fruta {i + 1}: ")
    fruta["precio_unitario"] = float(input(f"Precio unitario de {fruta['nombre']}: "))
    fruta["cantidad"] = int(input(f"Cantidad de {fruta['nombre']} que desea agregar: "))
    
    frutas.append(fruta)

def costo_total(frutas):
    total = 0
    for fruta in frutas:
        total += fruta["precio_unitario"] * fruta["cantidad"]
    return total

print(f"El costo total del salpicón es: ${costo_total(frutas)}")

frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"], reverse=True)
print("Frutas ordenadas de mayor a menor costo: ")
for fruta in frutas_ordenadas:
    print(f"Nombre: {fruta['nombre']}, Precio Unitario: ${fruta['precio_unitario']}")

frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"])
fruta_barata = frutas_ordenadas[0]
fruta_cara = frutas_ordenadas[-1]

print(f"La fruta más barata es: {fruta_barata['nombre']} con un precio unitario de ${fruta_barata['precio_unitario']}")
print(f"La fruta más cara es: {fruta_cara['nombre']} con un precio unitario de ${fruta_cara['precio_unitario']}")

#David Toro Montoya
#Tomas Henao Arroyave