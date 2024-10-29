from mercapy import Mercadona

mercadona = Mercadona("14001")
busqueda = mercadona.search(input("Introduzca el producto a buscar: "))
if len(busqueda) == 0:
    print("No se ha encontrado nada.")
else:
    for producto in busqueda:
        print("--------", producto.id, "------")
        print("Nombre:", producto.name)
        print("Descripción:", producto.description)
        print("Marca:", producto.brand)
        print("Precio:", producto.unit_price, "€")
        if producto.is_new:
            print("Novedad: Sí")
        else:
            print("Novedad: No")