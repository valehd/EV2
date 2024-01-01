def agregar_compra(lista_compras):
    monto_compra = input("Ingrese el monto de la compra: ")
    monto_compra = float(monto_compra)
    lista_compras.append(monto_compra)
    print("monto de compra agregado.")


def mostrar_compras(lista_compras):
    for idx, monto_compra in enumerate(lista_compras, start=1):
     print(f"{idx}. {monto_compra}")

def mostrar_total(lista_compras):
    if len(lista_compras) == 0:
        return 0
    total_gastado = sum(lista_compras)
    print(f"Total gastado: ${total_gastado}")
    return total_gastado


def main():
    compras = list()
    total_gastado = 0


    while True:
       print("Menú:")
       print(" 1. Agregar compra")
       print(" 2. Mostrar compras")
       print(" 3. Mostrar total gastado")
       print(" 4. Salir")

       opcion = int(input("Ingrese el número de la operación deseada: "))

       if opcion == 4:
          print("Saliendo...Hasta la próxima!!")
          break

       if opcion == 1:
        agregar_compra(compras)
       elif opcion == 2:
         mostrar_compras(compras)
       elif opcion == 3:
        total_gastado = mostrar_total(compras)

       else:
        print("Opción inválida")

main()