from mercapy import Mercadona

mercadona = Mercadona("14010")
print("País del Mercadona elegido:", mercadona.language)
aBuscar = ""
while aBuscar != "*":
    aBuscar = input("Introduzca el producto a buscar (* para salir):\n")
    if aBuscar != "*":
        busqueda = mercadona.search(aBuscar)
        longitud = len(busqueda)
        print("Resultados:", longitud)

        if longitud == 0:
            print("No se ha encontrado nada.")
        else:
            if input("¿Continuar? (Y/N): ").lower() == "y":
                encabezado = ""
                contador = 0
                for producto in busqueda:
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

                print("-" * len(encabezado))
    else:
        print("Saliendo...")