meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
         "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

departamentos = ["Ropa", "Deportes", "Juguetería"]

ventas = [[0 for _ in departamentos] for _ in meses]

def insertar_venta():
    mes = int(input("Mes (1-12): ")) - 1
    depto = int(input("Departamento (1=Ropa, 2=Deportes, 3=Juguetería): ")) - 1
    valor = int(input("Monto de venta: "))
    ventas[mes][depto] = valor
    print(f"Venta registrada: {meses[mes]} - {departamentos[depto]} = {valor}\n")

def buscar_venta():
    mes = int(input("Mes a buscar (1-12): ")) - 1
    depto = int(input("Departamento (1=Ropa, 2=Deportes, 3=Juguetería): ")) - 1
    print(f"Resultado: {ventas[mes][depto]} para {meses[mes]} - {departamentos[depto]}\n")

def eliminar_venta():
    mes = int(input("Mes a eliminar (1-12): ")) - 1
    depto = int(input("Departamento (1=Ropa, 2=Deportes, 3=Juguetería): ")) - 1
    ventas[mes][depto] = 0
    print(f"Venta eliminada en {meses[mes]} - {departamentos[depto]}\n")

def mostrar_tabla():
    print(f"{'Mes':<12}{'Ropa':>12}{'Deportes':>12}{'Juguetería':>12}")
    print("-" * 48)
    for i, mes in enumerate(meses):
        print(f"{mes:<12}{ventas[i][0]:>12}{ventas[i][1]:>12}{ventas[i][2]:>12}")
    print()

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar venta")
        print("2. Buscar venta")
        print("3. Eliminar venta")
        print("4. Mostrar tabla de ventas")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            insertar_venta()
        elif opcion == 2:
            buscar_venta()
        elif opcion == 3:
            eliminar_venta()
        elif opcion == 4:
            mostrar_tabla()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción inválida\n")

if __name__ == "__main__":
    menu()

