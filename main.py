
productoReloj = 10000
productoCollar = 11000
productoBrazalete = 12000
productoAnillo = 13000
productoAros = 14000
totalCompraUsuario = 0


valorSeleccionado = 0
conjuntoProductos = [productoReloj, productoCollar,
                     productoBrazalete, productoAnillo, productoAros]

producto = input(
      "Ingrese: \n 0. Seleccionar Reloj $10.000 \n 1. Seleccionar Collar $11.000 \n 2. Seleccionar Brazalete $12.000 \n 3. Seleccionar Anillo $13.000 \n 4. Seleccionar Aros $14.000 \n : ")
if int(producto) == 0:
      print("Selecciono Reloj")
      cantidadCompra = input("Ingrese cantidad a llevar: ")
      valorSeleccionado = productoReloj
else:
    if int(producto) == 1:
          print("Selecciono Collar")
          cantidadCompra = input("Ingrese cantidad a llevar: ")
          valorSeleccionado = productoCollar
    else:
      if int(producto) == 2:
          print("Selecciono Brazalete")
          cantidadCompra = input("Ingrese cantidad a llevar: ")
          valorSeleccionado = productoBrazalete
      else:
        if int(producto) == 3:
            print("Selecciono Anillo")
            cantidadCompra = input("Ingrese cantidad a llevar: ")
            valorSeleccionado = productoAnillo
        else:
          if int(producto) == 4:
              print("Selecciono Aros")
              cantidadCompra = input("Ingrese cantidad a llevar: ")
              valorSeleccionado = productoAros
            
productoSeleccionado = int(producto)
cantidadSeleccionada = int(cantidadCompra)
totalCompra = cantidadSeleccionada*valorSeleccionado
totalCompraIva = totalCompra*1.19
  
print("El total de su boleta es: $ " + str(totalCompraIva))
print("¡Gracias por su compra!")