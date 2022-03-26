
#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuación preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta información en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el código, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco más del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su año de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#¿Cómo lo haremos?, usaremos una variable para guardar el resultado del cálculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuación le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta información para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos será escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ también estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de línea que ocurran en el código se considerarán como parte del string.
# Si no estás convencido, prueba el funcionamiento reemplazando los delimitadores por "


# print("Bienvenidos a ...")
# print("""
#     _       _________ _______  _______             _______  _______  ______  
#    ( (    /|\__   __/(  ____ \(  ____ )|\     /|  (  ____ )(  ____ \(  __  \ 
#    |  \  ( |   ) (   | (    \/| (    )|( \   / )  | (    )|| (    \/| (  \  )
#    |   \ | |   | |   | (__    | (____)| \ (_) /   | (____)|| (__    | |   ) |
#    | (\ \) |   | |   |  __)   |     __)  \   /    |     __)|  __)   | |   | |
#    | | \   |   | |   | (      | (\ (      ) (     | (\ (   | (      | |   ) |
#    | )  \  |___) (___| (____/\| ) \ \__   | |     | ) \ \__| (____/\| (__/  )
#    |/    )_)\_______/(_______/|/   \__/   \_/     |/   \__/(_______/(______/                                    
                                                                         
# """)

# #Primera interacción. Solicitamos al usuario que ingrese su nombre,
# #y lo guardamos en una variable de tipo str
# print()
# nombre = str(input("Para empezar, dime como te llamas. "))
# print()
# print("Hola ", nombre, ", bienvenido a Mi Red")
# print()

# apellido = str(input("¿Cuál es tu apellido? "))
# print()
# print("Así que es", apellido+". Que lindo apellido")
# print()

# #Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
# #dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
# #¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente línea?
# agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
# print()
# edad = 2021-agno-1
# print(edad)
# print()

# sexo = str(input("¿Cuál es tu sexo? "))
# print()

# #Tercera interacción. Solicitamos la estatura, medida en metros.
# #Utilizamos la conversión a 'int', y una expresión para convertir esto
# #a una medida en metros y centímetros
# estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
# estatura_m = int(estatura)
# estatura_cm = int( (estatura - estatura_m)*100 )
# print()

# #Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
# num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
# print()

# #por mi.
# pais = str(input("¿De que país eres? "))
# print()
# #Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
# print()
# print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
# print("--------------------------------------------------")
# print("Nombre:  ", nombre)
# print("Apellido:", apellido)
# print("Edad:    ", edad, "años")
# print("Sexo:    ", sexo)
# print("País:    ", pais)
# print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
# print("Amigos:  ", num_amigos)
# print("--------------------------------------------------")
# print("Gracias por la información. Esperamos que disfrutes con Mi Red")
# print()

# continuar = True
# while continuar: 

#     escribir_msj = str(input("¿Quieres escribir un mensaje? (S/N)"))

#     if escribir_msj == "S" or escribir_msj == "s" or escribir_msj =="" or escribir_msj == "Si" or escribir_msj == "si" or escribir_msj == "sí" or escribir_msj == "Sí":
#         mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
#         print()
#         print("--------------------------------------------------")
#         print(nombre,apellido, "dice:", mensaje)
#         print("--------------------------------------------------")
#         cambio_nombre = input("¿Deseas cambiar tu nombre? (S/N)")
#         if cambio_nombre ==  "S" or cambio_nombre == "s":
#             nombre = input("¿Cómo es tu nuevo nombre?")
#             print("Se ha actualizado tu nombre, gracias por todo", nombre)
#             ver_datos = input("¿Quieres ver todos tus datos con tu nombre actualizado? (S/N)")
#             if ver_datos == "S" or ver_datos== "s":
#                 print("--------------------------------------------------")
#                 print("Nombre:  ", nombre)
#                 print("Apellido:", apellido)
#                 print("Edad:    ", edad, "años")
#                 print("Sexo:    ", sexo)
#                 print("País:    ", pais)
#                 print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
#                 print("Amigos:  ", num_amigos)
#                 print("--------------------------------------------------")

#     elif escribir_msj == "N" or escribir_msj == "n" or escribir_msj == "No" or escribir_msj == "no":
#         continuar = False
#     else:
#         print("Por favor, escribe una afirmación o una negación")

# print("Gracias por usar Niery Red. ¡Nos vemos Ñery!")






def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
    _       _________ _______  _______             _______  _______  ______  
   ( (    /|\__   __/(  ____ \(  ____ )|\     /|  (  ____ )(  ____ \(  __  \ 
   |  \  ( |   ) (   | (    \/| (    )|( \   / )  | (    )|| (    \/| (  \  )
   |   \ | |   | |   | (__    | (____)| \ (_) /   | (____)|| (__    | |   ) |
   | (\ \) |   | |   |  __)   |     __)  \   /    |     __)|  __)   | |   | |
   | | \   |   | |   | (      | (\ (      ) (     | (\ (   | (      | |   ) |
   | )  \  |___) (___| (____/\| ) \ \__   | |     | ) \ \__| (____/\| (__/  )
   |/    )_)\_______/(_______/|/   \__/   \_/     |/   \__/(_______/(______/                                    
                                                                         
    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    return 2017-agno-1

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
    return amigos

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje púlico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Intentalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

print("Bienvenidos a ...")


# Ahora empieza el programa principal.

mostrar_bienvenida()
nombre = obtener_nombre()
print()
print("Hola ", nombre, ", bienvenido a Ñery Red")
print()
edad = obtener_edad()
(estatura_m, estatura_cm) = obtener_estatura()
num_amigos = obtener_num_amigos()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con la Ñery Red")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    # Mostramos el menu
    opcion = opcion_menu()

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = obtener_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    #Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        (estatura_m, estatura_cm) = obtener_estatura()
        num_amigos = obtener_num_amigos()
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar Niery Red. ¡Nos vemos Ñery!")










