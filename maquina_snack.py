# Definimos los snacks de la maquina (una lista con diccionarios)
snacks = [
                {'id' : 1, 'nombre' : 'Patatas', 'precio' : 2},
                {'id' : 2, 'nombre' : 'Chocolate', 'precio' : 3}
            ]


# Definimos el ticket donde se agregaran los snack comprados
ticket = []


# Definimos la funcion para mostrar el menu
def mostrar_menu():
    print(f'--- SNACKS DISPONIBLES ---')
    for stock in snacks:
        print (f'ID: {stock['id']} -> {stock['nombre']} - {stock['precio']}$')

    print (f'\n--- MENÚ MÁQUINA SNACKS ---\n',
           f'   1. Comprar Snack\n',
           f'   2. Mostrar ticket\n',
           f'   3. Salir')
    opciones = int(input(f'\nSelecciona una opcion (1-3): '))
    return opciones


# Definimos la funcion para comprar snack (opcion 1)
def comprar_snack():
    id_snack_comprar = int(input(f'Selecciona snack a comprar (id): '))
    for detalles in snacks:
        if detalles['id'] == id_snack_comprar:
            id = detalles['id']
            nombre = detalles['nombre']
            precio = detalles['precio']
            producto_ticket = {'id': id, 'nombre' : nombre, 'precio': precio}
            ticket.append(producto_ticket)
            print(f'Se ha añadido el siguiente producto al ticket -----> '
                  f'ID: {detalles['id']} -> NOMBRE: {detalles['nombre']} - '
                  f'PRECIO: {detalles['precio']}$\n')
            return
    print (f'Producto no encontrado\n')


# Definimos la funcion para mostrar el ticket (opcion 2)
def mostrar_ticket():
    suma = 0
    print("---------- TICKET DE COMPRA ----------\n")
    for id_producto, detalle_ticket in enumerate(ticket):
        print(f'PRODUCTO {id_producto +1} --- '
              f'ID: {detalle_ticket['id']} -> NOMBRE: {detalle_ticket['nombre']} - '
              f'PRECIO: {detalle_ticket['precio']}$\n')
        suma += detalle_ticket['precio']
    print(f'EL TOTAL DE COMPRA ES: {suma}')
    print("---------------------------------------\n")


salir = False
while not salir:
    llamar_funcion_mostrar_menu = mostrar_menu()
    if llamar_funcion_mostrar_menu <1 or llamar_funcion_mostrar_menu > 3:
        print (f'Selecciona una opcion entre 1 y 3\n')
    else:
        print(f'La opcion elegida es {llamar_funcion_mostrar_menu}\n')
        if llamar_funcion_mostrar_menu == 1:
            comprar_snack()
        if llamar_funcion_mostrar_menu == 2:
            mostrar_ticket()
        if llamar_funcion_mostrar_menu == 3:
            salir = True
