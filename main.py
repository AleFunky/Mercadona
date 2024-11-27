from mercapy import Mercadona
import math

def buscador(mercadona):
    a_buscar = ""
    while a_buscar != "*":
        a_buscar = input("Introduzca el producto a buscar (* para salir):\n")
        if a_buscar != "*":
            busqueda = mercadona.search(a_buscar)
            longitud = len(busqueda)
            print("Resultados:", longitud)

            if longitud == 0:
                print("No se ha encontrado nada.")
            else:
                contador = 0
                pagina = 0
                total_paginas = math.ceil(longitud / 10)
                for producto in busqueda:
                    if contador % 10 == 0:
                        if input("¿Continuar? (Y/N): ").lower() == "n":
                            break
                        else:
                            pagina += 1
                            print("----------------------------------------------------")
                            print(f"    Página {pagina}/{total_paginas}")
                            print("----------------------------------------------------")

                    contador += 1
                    encabezado = f"--------{producto.id} ({contador}/{longitud})--------"
                    print(encabezado)
                    print("Nombre:", producto.name)
                    print("Descripción:", producto.description)
                    print("Marca:", producto.brand)
                    print("Precio:", producto.unit_price, "€")
                    if producto.is_new:
                        print("Novedad: Sí")
                    else:
                        print("Novedad: No")
        else:
            print("Saliendo...")

def novedades(mercadona):
    nuevos_productos = mercadona.get_new_arrivals()
    longitud = len(nuevos_productos)
    print("Número de novedades:", longitud)

    if longitud == 0:
        print("No hay novedades por el momento.")
    else:
        contador = 0
        pagina = 0
        total_paginas = math.ceil(longitud / 10)
        for producto in nuevos_productos:
            if contador % 10 == 0:
                if input("¿Continuar? (Y/N): ").lower() == "n":
                    break
                else:
                    pagina += 1
                    print("----------------------------------------------------")
                    print(f"    Página {pagina}/{total_paginas}")
                    print("----------------------------------------------------")

            contador += 1
            encabezado = f"--------{producto.id} ({contador}/{longitud})--------"
            print(encabezado)
            print("Nombre:", producto.name)
            print("Descripción:", producto.description)
            print("Marca:", producto.brand)
            print("Precio:", producto.unit_price, "€")


mercadona = Mercadona("14010")
print("País del Mercadona elegido:", mercadona.language)
opcion = -1
while opcion != 0:
    print("Mercadona Mercadona")
    print("1 - Busqueda de productos")
    print("2 - Obtener novedades")
    print("0 - Salir")
    while True:
        try:
            opcion = int(input("> "))
            break
        except ValueError:
            print("Opción incorrecta")

    if opcion == 0:
        print("Saliendo del Mercadona...")
    elif opcion == 1:
        buscador(mercadona)
    elif opcion == 2:
        novedades(mercadona)
    else:
        print("Opción incorrecta.")

print("Adiós")
