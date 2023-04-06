"""<!-- Comentario --> / html
// Comentario / CSS
/* Comentario / Js """

"""var miVariable;
let miOtraVariable;"""

# mi_variable = "Rodrigo"
# mi_Edad = 28

# nombre = input("Ingrese su nombre")
# print("Bienvenido" + nombre)

# edad = str(input("Ingrese su edad: "))
# edad_aumentada = edad + 1
# print ("Usted tiene " + edad + " años." + "y el próximo cumpleaños usted tendrá: " + str(edad_aumentada))
# print (f"Usted tiene " + edad + " años." + "y el próximo cumpleaños usted tendrá: " {edad_aumentada})

productoReloj = 10000
productoCollar = 11000
productoBrazalete = 12000
productoAnillo = 13000
productoAros = 14000


conjuntoProductos = [productoReloj, productoCollar,
                     productoBrazalete, productoAnillo, productoAros]
cantidadProductos = input(
    "Ingrese: \n 0. Seleccionar Reloj \n 1. Seleccionar Collar \n 2. Seleccionar Brazalete \n 3. Seleccionar Anillo \n 4. Seleccionar Aros \n : ")
if int(cantidadProductos) == 0:
    print("Selecciono Reloj")
    cantidadCompra = input("Ingrese cantidad a llevar: ")
else:
    if int(cantidadProductos) == 1:
        print("Selecciono Collar")
        cantidadCompra = input("Ingrese cantidad a llevar: ")
    else:
      if int(cantidadProductos) == 2:
        print("Selecciono Brazalete")
        cantidadCompra = input("Ingrese cantidad a llevar: ")
      else:
        if int(cantidadProductos) == 3:
          print("Selecciono Anillo")
          cantidadCompra = input("Ingrese cantidad a llevar: ")
        else:
          if int(cantidadProductos) == 4:
            print("Selecciono Aros")
            cantidadCompra = input("Ingrese cantidad a llevar: ")
          
cantidad_Productos = int(cantidadProductos)
cantidad_Compra = int(cantidadCompra)
totalCompra = cantidad_Compra*cantidad_Productos

print("El total neto de su compra es: $ " + str(totalCompra))

respuestaUsuario = str(input("¿Desea agregar algo más?(Si/No) :"))
if respuestaUsuario == ("Si" or "si"):
  cantidadProductos;
  cantidadCompra;
