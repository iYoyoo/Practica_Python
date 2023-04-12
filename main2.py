"""num = int(input("Cuantos productos :"))
costo_producto = num * 2.00
costo_envio = num * 0.50
if num >= 30:
    costo_envio = 0
total = costo_producto + costo_envio
print (total)"""

"""edad = int(input("Ingresa tu edad :"))
if edad >= 18:
    if edad < 30:
        print ("Eres un joven y mayor de edad")
    elif edad >= 30 and edad < 60:
        print ("Eres un adulto maduro")
    else:
        print ("Eres un adulto mayor")
else:
    print ("Eres menor de edad")"""

"""listado_usuarios = {"Rodrigo": "miClave", "Sebastian": "miclave", "Maria": "claveMi"}
usuario = input("Escriba su nombre de usuario: ")
password = input("Escriba su contraseña: ")

if usuario in listado_usuarios:
    if password in listado_usuarios[usuario]:
        print(f"Bienvenido {usuario}")
    else:
        print("Clave incorrecta")
else:
    print (f"No se ha encontrado usuario con el nombre {usuario} ni clave.")"""

combustible = input("Necesito combustible? (S/N) :")
if combustible == "S":
    dinero = input("Tengo dinero? (S/N: ")
    if dinero == "N":
        print("Sacando dinero del cajero...")
    print ("Cargando combustible...")
print("Yendo al trabajo")