
#Una empresa que forma parte de la industria automotriz solicita un sistema que permita a los empleados de la misma llevar cuenta de los vehículos que vendieron. 
#Cada vehículo tendrá asignado una patente y un precio. los datos de los vendedores serán almacenados teniendo en cuenta que cada vendedor tendrá un nombre y un DNI. 
#Las ventas de cada vendedor serán guardadas en un archivo (o diccionario si no se usan archivos) 
#junto con su nombre mientras que también el programa será capaz de presentar distintas métricas como:
#cantidad de ventas totales y porcentaje de las ventas realizadas por cada vendedor.



autos = {}
vendedores = {}


while True:
    print("\nSistema de Gestión de Stock de Autos y Ventas")
    print("1. Cargar autos")
    print("2. Cargar vendedor")
    print("3. Registrar venta")
    print("4. Mostrar métricas de ventas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        patente = input("Ingrese la patente del auto: ")
        try:
            precio = int(input("Ingrese el precio del auto: "))
            autos[patente] = precio
            print(f"Auto {patente} agregado con precio {precio}.")
        except Exception:
            print("Precio no válido.")

    elif opcion == "2":
        dni = input("Ingrese el DNI del vendedor: ")
        nombre = input("Ingrese el nombre del vendedor: ")
        vendedores[dni] = {"nombre": nombre, "ventas": 0}
        print(f"Vendedor {nombre} agregado con DNI {dni}.")

    elif opcion == "3":
        dni_vendedor = input("Ingrese el DNI del vendedor: ")
        if dni_vendedor not in vendedores:
            print("Vendedor no encontrado.")
        else:
            patente_auto = input("Ingrese la patente del auto vendido: ")
            if patente_auto not in autos:
                print("Auto no encontrado.")
            else:
                precio = autos[patente_auto]
                vendedores[dni_vendedor]["ventas"] += precio
                del autos[patente_auto]
                print(f"Venta registrada: {vendedores[dni_vendedor]['nombre']} vendió el auto {patente_auto} por {precio}.")

    elif opcion == "4":
        # Calcular el total de ventas
        total_ventas = 0
        for vendedor in vendedores.values():
            total_ventas += vendedor["ventas"]
        print(f"Cantidad de ventas totales: {total_ventas}")

        # Calcular y mostrar el porcentaje de ventas por cada vendedor
        for dni, vendedor in vendedores.items():
            if total_ventas > 0:
                porcentaje = (vendedor["ventas"] / total_ventas) * 100
            else:
                porcentaje = 0
            print(f"{vendedor['nombre']}: {vendedor['ventas']} ({porcentaje:.2f}%)")


    elif opcion == "5":
        print("Saliendo del sistema.")
        break

    else:
        print("Opción no válida.")
