"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?

cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
programador:
    vaya
mente:
    no te pide nada el gusto mono


"""

# creando la lista vacia
listaRegistro = []
contador = 0
suma = 0
while contador < 1:
    print("¿Desea agregar un cliente?Escriba '1' para sí y '0' para no")
    respuesta = int(input("inserte su rspuesta: "))

    if respuesta == 1:
        cliente = input("nombre del cliente: ")
        producto = input("producto: ")
        costo = float(input("costo ($0.00): "))
        suma = suma + costo

        # punto de programa
        # registro = {"cliente": cliente, "producto": producto, "costo": costo}
        registro = dict(cliente=cliente, producto=producto, costo=costo)
        # como agrego un elemento nuevo a una lista?
        listaRegistro.append(registro)
        # dejar de ocupar la variable registro
        # registro = None
        contador = 0
    else:
        print("El total de costos hasta el momento es de: " + str(suma))
        contador += 2

for registro in listaRegistro:
    print(registro)
