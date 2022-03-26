# Un archivo python debe tener la extensión .py
# La consola de python se abre en la pestaña tools, en la parte "Python or Debug Consol"
# Para ejecutar un codigo, hay que darle a "run" en la parte de herramientas.
# O sino en la pestaña del codigo que queremos correr. Apretar click derecho y en run


#Python es un lenguaje de alto nivel, el cual se hace entendible al ser humano, a diferencia del lenguaje maquina
#el cual se compone de 0 y 1( 0 no pasa corriente, 1 pasa corriente), los cuales son impulsos eléctricos.
#Al ser un lenguaje de programación, python maneja un conjunto de valores, y a estos se les llama tipos de datos

#----------------------------------------------------------------------------
#Semana 2
#Tipos de Datos
#CUales tipos de datos hay?
#Tipos númericos: int, float (int son números enteros, float son decimales)
#Tipos de texto: str (van a ser secuencias o cadenas de caracteres. Siempre se ponen entre comillas)
#Tipos lógicos (booleanos): bool (False True). A diferencia de JS, los booleanos comienzan con mayúsculas.
#Apunte por fuera de clase. También están los tipos de datos object y function.

#Para saber que tipo de dato estamos usando? Si escribimos el método type() y adentro de los parentesis, ponemos el
#valor del dato que queremos usar (igual que el operador typeof de JS). Type nos devolverá a que clase de tipo de dato pertenece. EJ:
#type(42) ... Esto nos devolverá <class 'int'>
#type("Hola mundo") ... Esto nos devolverá <class 'str'>
#type(bool) ... Esto nos devolverá <class 'bool'>


#----------------------------------------------------------------------------

# Operadores y expresiones

#Necesitamos expresar operaciones. Utilizamos símbolos: operadores. Expresamos cálculos: expresiones
# Operadores para tipos numéricos
# Operadores osbre int y float:
# +(Suma)5+5   -(Resta)5-5   *(Multiplicación)5*5   /(División) 5/5
# -(Inverso aditivo) -5  **(Exponenciación)5**5  //(División Entera) 7//5   %(Modulo) 7%5
#La división entera entregará solamente el coeciente. Ignorando el resto.


#Expresiones con más de un operador se evalúan en precedencia. Operadores con = precedencia se resuelven en orden
#de asociatividad.

#() Utilizando paréntesis damos prioridad primero a ciertas expresiones.
#En la asociatividad, siempre iran primero la exponenciación (de derecha a izq).Ej: 2**3**2 =512
# Luego las unarias + , -. Ej: -2 ** 2 = -4 ... Acordarse que cuando se hace el exponente, no se cuenta al -, a no ser que englobe la operación entre parentesis y por fuera el exponente
# Tercero las multiplicaciónes, Divisiones, divisiones enteras y modulo (izq a derecha) Ej: 15/3*2 = 10
# Y por ultimo los binarios (suma y resta, de izq a derecha) Ej: 3-4+5 =4

#Operadores de comparación.
#Se aplican a int o float.
# < <= > >= != ==
# 5<5.1 Menor que.  3 >= 5 Mayor o igual que.  3!= 5 Distinto que.  6 == 9 Igual que

# Operadores lógicos
# Se aplican a bool
# not and or
# Siempre entrega un tipo bool.

# 5//4 > 3 or 2<5**2

#Los operadores de comparación tienen menor precedencia que los numéricos.
#"< <= > >= != ==  (de izq a derecha)
#not
#and (izq a derecha)
#or  (izq a derecha)

# operadores para str
# + concatenación. Ej: "Yo soy " + "tu padre"  = "Yo soy tu padre"
# * repetición. EJ: "Ja" * 4 = JaJaJaJa

#----------------------------------------------------------------------------

# Manipulación de datos. Conversiones de tipos.
# cuando se divide un int con un float, obtenemos un float.
# cuando ponemos un str junto a un int o float. Obtenemos un error. EJ: "Son las " + (3+12). Dará error.
# En python no se puede mezclar una operación númerica y un str sin hacer algo antes. A diferencia de JS que daría Son las 15

# Para que funcione el mismo. Hay que utilizar el metodo str().
# También está el método int() y float(). El primero convierte a entero, y el segundo a decimal.
# También el método bool()
# "Son las " + str(3 + 12) = 'Son las 15'
# int("3") + 2 = 5
# float("3.5") + 12 = 15.5
# no se pueden hacer con caracteres que no sean numeros o dará error
# bool(0) = False
# bool("") = False
#si se le agrega algo al método bool, siempre dará true, salvo 0 y ""
#bool(False) = True
#str(8+1.76) + " segundos) = '9.76 segundos'
#str(3<5 and 9.76< 10) = 'True'

#----------------------------------------------------------------------------

# Variables.
# Las variables pueden almacenar datos en nuestro computador y así poder reutilizarlos.
# Se recupera el vaor utilizando el nombre que le asignamos a la variable. La cuál se le asigna con un =
#Hay que ver la diferencia con el igual de una operación. Esta representa una ASIGNACIÓN

# llegada = 14
# llegada ... Esto dará 14.
# pesos_por_hora = 200
# (19-llegada)* pesos_por_hora    dará 1000
# llegada = 20
# salida = 22
# (salida - llegada) * pesos_por_hora    dará 400

# El valor de las variables se puede reeasignar otro valor.

# la asignación (=) se utiliza así :
# nombre = expresión
# el nombre al lado izquierdo y la expresión en el lado derecho

# Las variables deben comenzar con una letra o "_". Luego pueden seguir con letras, números, "_"
# Las mayúsculas y minúsculas importan. Van a ser distinto llegada que LLegada
# Las palabras reservadas no se pueden utilizar como nombre de variables.

#----------------------------------------------------------------------------

#Escribiendo en pantalla
#Para escribir en la pantalla, hay que utilizar el método print().
#print(expresión)
#mensaje = "Hola mundo"
#print(mensaje)  imprimirá Hola mundo
#print((3+5//4-2)-2**4+3*(7-2))    imprimirá 1
# Cada ejecución de print, hará un salto de linea. Por ende, para que no haga este salto de linea, hay que utilizar
# el mismo print. O sino, utilizar una asignación con una variable llamada end, que agregue un string vacio al final del print.
# print(expresion, end=str) ... A ese end, se le puede agregar cualquier valor string, que igualmente evitará el salto de linea.
# episodio = 2
# print("Episodio", episodio, "del libro")  imprimirá Episodio 3 del libro
# print("Episodio", episodio, end=" ")
# print("del libro)
# esto imprimirá Episodio 3 del libro

#También podemos asignarle que para cada separación de asignacación del print, con el sep=str) haya un caracter especifico. Ej:
# print(expresion, sep=str)
#print("-El tesoro","está", "en", sep="...")
# imprimirá -El tesoro...está...en

#----------------------------------------------------------------------------

#con la palabra reservada input haremos que el computador reciba el valor que el usuario le da a cierto elemento.
# Este método siempre entregará un str
# Entrada (input) => Programa => Resultado(output)
# variable = input(texto) => dará un resultado, que le asigno el usuario, el cual se guardará en una variable
#Ej:
# nombre = input("¿Cuál es tu nombre?")
# saludo = "Hola,"
# pregunta = "¿Cómo estás hoy?"
# print(saludo, nombre, pregunta)   Hola, (el nombre que le haya asignado al input) ¿cómo estás hoy?

# otro ej.
# Para cambiar el tipo de dato del input, hay que utilizar los métodos. int() float() etc.
# lec = int(input("¿Cuántas lecciones has visto?"))
# total = 15
# faltan = total - lec
# print("Te faltan ", faltan, "lecciones. ¡Ánimo!")





#----------------------------------------------------------------------------

# Semana 3 

# If-Else
# Sirve para cambiar el flujo del programa en base a una condición. 
#Una condición es una expresión que puede tomar uno de dos valores. Verdadero o falso, y una variable que guarda este tipo de valores sera de tipo bool. 
#Los operadores de comparación siempre dará un valor de tipo bool.
# También los operadores para tipos lógicos (not,and,or).
# Estructura básica:
# if condición: 
#     insrucción1
# else:
#     instrucción2

#Los espaciós dentro, se llama identación, en python es muy rígido el uso de estos espacios.
# Si la condición del if es falsa, se correrá la instrucción dentro del else.


# If
# A diferencia con el else, el if si no se cumple, no realizará ninguna otra instrucción, y seguirá con el programa 

# Se puede hacer un if sin else pero no un else sin un if



# Elif
# Es una forma más resumida que ir anidando if dentro de ifs. Se puede poner tantos elif como queramos. 
#No puede haber elif sin if

# if condición1: 
#   instrucción1
# elif condicion2:
#   instrucción2
# elif condicion3:
#   instrucción3
# ...
# else:
#   instrucciónN

# numero = int(input("Ingrese calidad del aire"))
# if numero>=0 and numero<=99:
#   print("Bueno")
# if numero>=100 and numero<=199:
#   print("Regular")
# if numero>=200 and numero<=299:
#   print("Alerta")
# if numero>=300 and numero<=499:
#   print("Preemergencia")
# else:
#   print("Emergencia")

# (numero = 163) Imprimirá regular y emergencia, ya que se está anidando al else con el último if. por ende, si no se cumple el último if, se imprime el emergencia.



#----------------------------------------------------------------------------

# WHILE


#Nos permite repetir tantas veces como queramos un conjunto de instrucciones
# Si la condición es True, se ejecuta el código dentro del while
# Si la condición es False, se ejecuta el código que sigue al while

# while condición: 
#   instrucciones


#----------------------------------------------------------------------------

#FOR

# Nos permite recorrer elemento por elemento una secuencia. Podemos generar secuencias con range ( no siempre se utilizará el range, para listas y otras cosas se utilizan otra función)
#Estructura:
# for variable in secuencia:
#   instrucciones

# temp = 0
# print("fº    cº")
# for temp in range(21): #A diferencia de js, aquí tiene un incremento automaticamente mientras la variable no llegue al valor anterior de range donde se especifica el numero
#   print(temp,"   ",int((temp-32)*5/9))

# range(fin) . Range crea una secuencia de números, que parte desde 0 y llega hasta fin -1.
# for i in range(7):
#   print(i) # corre de 0 a 6 (7 veces). pero no muestra el 7, porque ya recorrio 7 números

#range puede tener varios parametros
#range(inicio,fin) Crea una secuencia de números que parte desde inicio y llega hasta fin-1.
# for i in range(8,14):
#   print(i) #Mostrará hasta el número 13, porque, aunque comienza en el 8, está termina en el fin-1

#Si recibe 3 parametros, range(inicio, fin, paso) 
# for i in range(4,101,3): # este crea una secuencia de números, que parte desde inicio y llega hasta fin-1 avanzando de a paso números.
#   print(i)


#Instrucción de ciclo:for
# for variable in range (i,j,k):
#   instrucciones
#Genera secuencia desde i hasta j-1, con paso k, e itera sobre ella (i,k opcionales)



#----------------------------------------------------------------------------

# Funciones
# Son fragmentos de código que recibe parámetros, ejecuta acciones y retronan un resultado. Estas sirven para poder reutilizar codigo en el programa.

#elementos que recibe una función para trabajar con ellos. Variables que usa la función. Se entregan al llamar a la función, según la necesidad.


# Las funciones se declaran con def
#Estructura:
# def func(parametr1,parametro2,...):
#     ...
#     ...

# Los parametros quedan determinados al escribir el codigo de la funcion

#al llamar a una funcion, se entregan los datos o variables que se utilizaran como valores de los parametros.

# Valor retorno
# Valor que entrega la función al terminar de ejecutarse. Se puede igualar a una variable
#Se utiliza la palabra clave return.
# El valor retorno constituye el termino de la funcion. Se termina al realizar su ejecución.



#Funciones contenidos en python
# Existen muchas librerías o módulos ya programados.
#Estas relizan tareas de todo tipo.

#ej: random y math son ejemplos. Permiten realizar acciones u operaciones cotidianas con un simple llamado a una funcion.
# Random permite generar números pseudoaleatorios
#Math permite realizar cálculos complejos y acceder a constatnes conocidas como pi o e.

#para poder importar un modulo en python existen varios metodos.
# El primero es con la sentencia import seguida del nombre del módulo deseado. Ej:
# import <nombre_modulo> Ej: import math
#estructura:
# import modulo
# modulo.funcion(argumentos)

# Ej: 
# import math
# math.sin(0)


#Segundo metodo.
#Esta consiste en importar unicamente los elementos que vamos a ocupar dentro de nuestro programa 
#Esta se realiza por medio de la sentencia from, seguida del nombre del modulo,y luego la palabra clave import, seguida de los elementos necesarios. from <nombre_módulo> import <elemento1>, <elemento2> Ej:
# from math import pow, sqrt
#Estructura: 
# from modulo import funcion
# funcion(argumentos)

#Ej:
# from random import uniform
# uniform(0,1)


#Tercer método.
# esta es una variación de la anterior, la cual consiste en darle nombres especiales a los elementos importados para evitar que coincida con algun nombre que nosotros hayamos usado en nuestro programa. Se utiliza la palabra as luego del elemento importado from <nombre_módulo> import <elemento1> as <alias> Ej:
# from math import e as euler
#Estructura: 
# from modulo import funcion as mifun
# mifun(argumentos)

#Ej:
# from random import randint as rnd
# rnd(5,10)


# Cuarto método (no recomendado)
# Este consiste en importar todos los elementos del modulo con el nombre que estaba definido en la librería. Esta se hace escribiendo un asterisco luego del import . from <nombre_módulo> import *. Ej:
# from math import *
#Estructura: 
# from modulo import *
# funcion(argumentos)

#Ej:
# from random import *
# uniform(0,1)




#ejemplo de función de lanzamiento de un dado por medio de la generación de un numero aleatorio entre 1 y 6. Luego, dependiendo del valor que hayamos obtenido, se multiplica el valor por pi o e.

# from random import randint as rnd
# from math import pi, e 

# lanzamiento = rnd(1,6)
# if lanzamiento < 4:
#     print(pi* lanzamiento)
# else:
#     print(e*lanzamiento)

#funcion para mostrar el numero de digitos de un numero
# def funcion_misteriosa(x):
#   c=0
#   while x!=0:
#     c+=1
#     x = x//10
#   return print(c)

# funcion_misteriosa(10)

# Estructura básica de funciones.
#Comienzan con la palabra clave def y luego se escribe el nombre de la función, luego de esta se escriben los parentesis, y si hay parametros se escriben dentro del mismo. luego se escriben los dos puntos. Dentro de la función se escribe el código y los retornos, estos tienen que ir identados. 

# def nombre(param1,param2,...,paramN):
#   #aquí va el código de la función 
#   #y todo lo relacionado, las
#   #variables usadas, los retornos
#   valor=0
#   return valor

#Ej:
# def max_divisor(n):
#   maximo_actual = 0
#   i = 1
#   while i < n:
    #     if n % i == 0:
    #         maximo_actual = i
    #     i+=1
    # return maximo_actual

#Invocación de funciones y scope.

# La invocación es el llamado de la función. Esto lo realizamos cuando queremos ejecutar la función definida. Sin invocación, el código nunca se ejecuta
# se invoca luego de definirla. 
#Se puede, opcionalmente, igualar un llamado de función a una variable: 
# Ej: 
# def calculo(numero):
#     resultado = (numero - 3 )** 3
#     return resultado

# salida = calculo(5)


#Scope, el scope de una funcion corresponde al manejo de las variables dentro de la misma.
#Variables definidas dentro de una función no existen fuera de ella.
#ej: 
# def es_par(numero):
#     divisor = 2
#     if numero % divisor == 0:
#         return True
#     else:
#         return False


# print(divisor) #Dará error, ya que la variable está definida dentro de la función y no fuera de ella.

#el hecho de que las variables "mueran" al terminar la función evita errores. 
# A estas variables se les llama variables locales, y solo existen dentro de la función que las define.


#Modulos de funciones.
# Un archivo de python con la extensión .py es un módulo
# los módulos tienen conjuntos de funciones y constantes importables desde cualquier otro programa. Como ya hemos visto, los modulos se importa, entre otras formas, así:
# from modulo import elementos
#o
# import modulo

#Podremos crear distintos archivos python y importarlos segun nuestras necesidades, ejemplo: Creamos un archivo para nuestro programa y otro que contenga funciones y metodos.
#  Ej:
# from modulo_funciones import es_par     #importamos modulo_funciones a el programa actual
# numero = int(input("ingrese nº: "))
# if es_par(numero):
#   print("Su numero es par!")
# else:
#   print("su numero es impar!")

#Cuando hay muchas funciones, es muy útil hacer modulos. ESta separación clarifica y ordena los grandes proyectos




# función que retorne true cuando no se cumple la condición gracias al not
# def funcion(x):
#   n = 3
#   return not bool(x%n)
# print(funcion(9))
# print(funcion(10))



# Hecho por mi
from typing import Text


def mcd(n1,n2):
    num = min(n1,n2)
    while num > 1:
        if n1% num == 0 and n2%num == 0:
            break;
        num -=1;
    return num


mcd(10,15)


def exponente(n):
    num = 1;
    while 2**num <= n:
        num+= 1
    return num-1

exponente(5)


def panprimo(n):
    def esprimo(n):
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    letra = str(n);
    ej = "1000000000"
    if len(letra) < len(ej):
        return False
    elif letra.find("1") == -1 or letra.find("2")== -1  or letra.find("3")== -1  or letra.find("4")== -1  or letra.find("5")== -1  or letra.find("6")== -1  or letra.find("7")== -1  or letra.find("8")== -1  or letra.find("9") == -1:  
        return False
    else:
        nums = int(letra[-3:])
        if esprimo(nums):
            return True
        return False
    
print(panprimo(10123457689))




# ---------------------------------------------------------------------------------------------


# Semana 5

# Tipo de dato 'str'(string)
# Los string se representan entre comillas. Estos pueden representar muchas cosas de la vida cotidiana. Desde nombres de personas a párrafos de libros, nums de telefonos, contenido de pagina web, etc.

# Es posible concatenar dos strings con el simbolo de más "+"
#  ej: print("Hola" + " Gente")

# La concatenación se puede hacer sobre strings mismos o sobre variables que contengan strings.

#  La otra operación es la repetición de strings, esto se usa con el operador de multiplicador "*". Esta operación concatena el string consigo mismo tantas veces como le indiquemos.
#  print("Hola" * 3).

#  Los strings son inmutables. Una vez definido un objeto, este no cambiará a menos que se defina nuevamente.


#  Manipulación de strings.

# Es posible seleccionar ciertos elementos de un string, según su posición en él.
# Los índices comienzan en 0.
#  Ej: print("Martes"[0])  ... Dará "M"

#Para seleccionar los símbolos del final de un string, utilizamos números negativos ( posición -1 es última letra, decrecen hacia la izquierda)

# Podemos seleccionar un cierto intervalo de símbolos del string indicándolo como string[inicio:final+1]. Conocido como slicing. 
# El final +1 es porque si ponemos final, este no incluye el final en sí, por eso hay que poner el numero que sigue.

#Símbolos Especiales
# Existen ciertos símbolos que no pueden escribirse directamente con el teclado(como una línea nueva). Para eso está el símbolo "\" en conjunto con alguna lera para indicarlos

#  "\n" Este indica una nueva línea
# print("Un párrafo.\nOtro párrafo.")

# Para pescribir una sola vez "\", hay que utilizar "\\". 
#  print("Para escribir un backslash, poner dos \\")



# Métodos sobre strings.

# Son funciones muy útiles y comunes.
#Una de ellas es len (abreviado de length, longitud). Retorna el largo del string que se pase como párametro.

# Existen otros para transformar todo un string a mayúsculas o minúsculas. Estos se hacen con string.upper() y string.lower()

# print("Martes".upper())  ...Mostrará 'MARTES'
# print("Martes".lower())  ...Mostrará 'martes'

# Otro método es strip, permite remover algún símbolo de los extremos del string. Se le pasa como parametro el simbolo a remover
# a = "Bien. Martes a las 5." 
# print(a.strip("."))  ... Mostrará 'Bien. Martes a las 5' 

#  El método replace, reemplaza algún símbolo del string. Con el símbolo antiguo y el nuevo como parámetros
# a= "hola!!1!"
#print(a.replace("1","!")) ... Mostrará 'Hola!!!!'


# Concepto de archivo
# Un archivo es toda información en un computador que se guarda en alguna parte. Esta se organiza en directorios (o carpetas), y detntro de ellos archivos.

# Cuando ocupamos archivos de tareas en programación? Cuando queremos guardar información aun cuando se haya terminado de ejecutar un programa. O queremos leer información que tegnamos en nuestro computador.

#  Para estas labores se ocupan los archivos. Hay muchos tipos: estos se ven en la terminación (.doc, .ppt, .txt)

# ¿Qué se puede hacer en python con estos archivos?. Lo necesario para comunicar esos datos a otras personas, o a nosotros mismos en el futuro. Estos podemos leerlos, escribirlos, copiarlos, etc.


#  Interactuando con archivos.
#  Para abrir un archivo, esta la función open. El archivo debe estar en la misma carpeta que el programa.
# Se le debe dar como parámetro el nombre del archivo (incluyendo la terminación despues del punto)
# a = open("archivo.txt")

#  La función open toma un segundo parámetro: el modo, este indica el modo del archivo. Si queremos leerlo o escribirlo.
#  "r" :solo lectura(read)
#  "w" :escritura(write)
#  Si no se le indica ningún parámetro, python entiende que solo es leer por defecto.

# Para poder leer el archivo y mostrarlo con un print u otro método, hay que utilizar el método read sobre la variable que guarda al objeto open
# lectura = open("arch.txt", "r")
# leer = lectura.read()
# read no lleva parámetros.

#  Para leer una sola línea del archivo, se puede utilizar el método .readline()
# Cada vez que se llama a la función, se lee la siguiente línea del archivo.

# leer = lectura.readline()
# print(leer)
# leer2 = lectura.readline()
# print(leer2)


# Guardando información.
# Para escribir en un archivo, debemos poner en el segundo parámetro de open, la "w" de write.
# Si el archivo existe, se borrará para crear uno nuevo. 

# Para escribir en dicho archivo, se utiliza el método write(), pasando como parámetro el string que se quiere escribir.
# escritura = open("arch.txt", "w")
# escritura.write("Esto se escribe en el archivo")

# Si se quiere escribir más líneas, se deben indicar con los saltos de línea mediante el símbolo "\n"
# escritura.write("Uno \nDos \nTres")

#Una vez terminado de leer o escribir un archivo, se tiene que cerrar con el método .close().
# archivo.close()  No toma parametros
# Al cerrarse se guarda correctamente.


# -------------------------------------------------------------------------------------------


# Listas
# Son secuencias de elementos. Elementos que pueden ser de cualquier tipo y se encuentran ordenados

#  ej de lista:
# no_olvidar = ["huevos","palta","lechuga","naranjas",7000]

# Tipo de dato:list
# se empiezan con los corchetes cuadrados.
# Estructura:
# [elemento0,elemento1,...,elementoN-1]

# podemos usar variables o/y expresiones para poder hacer una lista. EJ:
# mesa = 5
# producto ="espresso"
# cantidad = 2
# costo = 500
# pedido = [producto,mesa,cantidad,costo,cantidad*costo]
# print(pedido)

# Podemos poner listas, dentro de una lista.

# Se pueden crear listas vacías. Así:
# vacia1 =[]
# o
# vacia2 = list()

# Manipulación de listas.
# Modificando la lista
# Las listas son mutables, podemos modificar sus elementos sin tener que reescribir la lista completa.
# Para acceder a un elemento, tenemos que acceder a traves de un índice o posición
# no_olvidar = ["huevos","palta","lechuga","naranjas",7000]
# print(no_olvidar)
# print(no_olvidar[2]) 
# # Aquí accederemos a lechuga.
# # También podemos acceder a secciones de la lista. esto se hace separando el índice donde comenzaremos, hasta el que queremos acceder+1
# print(no_olvidar[1:4])
# # Aquí le indicamos que queremos acceder desde el índice 1 hasta el 3.
# # estructura del slicing ( para acceder en secciones)
# # lista[inicio:fin:step] (fin-1 sería)
# # Ej: si ponemos lista[2:7:2] esto hará que se agarre desde el indice 2 hasta el 7 pero en dos en dos.
# # Si omitimos uno de los limites es que no hay limite, si ponemos [2:] Entonces irá hasta el final de la lista.
# # si omitemos el primer elemento, decimos que empieza desde el inicio la lista ej: [:5:2] en este caso avanzando en dos en dos.
# # Si especificamos el step como menos uno o algun numero negativo, la lista se recorrerá en sentido inverso, desde el final hacia el inicio.


# #Podemos recorrer una lista con la construcción for-in 
# for elem in no_olvidar:
#     print("No olvides", elem)

# # podemos modificar los valores de cada posición 
# no_olvidar[1] = "queso"
# no_olvidar[4] = 10000 
# print(no_olvidar)
 

# Agregando y eliminando elementos de una lista
no_olvidar = ["huevos","palta","lechuga","naranjas",7000]

# Se pueden concatenar listas al igual que los strings. con +
# tambien = ["apio", "tomates"]
# no_olvidar = no_olvidar + tambien
# print(no_olvidar)
# También podemos repetir una lista con el * 
# print(tambien*2)

# Para agregar un elemento al final de la lista se utiliza el método append
# lista.append(elemento)
# no_olvidar.append("apio")
# print(no_olvidar)

# Para agregar mas elementos a una lista, tenemos que usar el metodo extend agregando una lista. Ya que si hacemos eso con append. lo que hará será crear una lista dentro de la lista. extend no hace eso, agrega los elementos de una lista en otra sin agregarlas como lista.
# list.extend(list)
#  no_olvidar.extend(["apio","tomates"])
# print(no_olvidar)

# # El método insert va a servir para agregar un elemento en el índice que nosotros deseemos.
# list.insert(index,elem)
# no_olvidar.insert(2,5000)
# print(no_olvidar)


# el metodo pop, elimina y retorna el elemento indicado con el indice de la lista. 
# lista.pop(n)
# comprado = no_olvidar.pop(0)
# Como guardamos en una variable el retorno del elemento eliminado, con esa variable vamos a saber que elemento fue el que eliminamos, y lo podemos agregar o hacer lo que queramos con dicho valor
# print(comprado)
# print(no_olvidar)

# Sacar de cualquier posición ( según ellos pero el método pop ya hace eso.)
# Segun internet, remove busca la coincidencia de valor y elimina y retorna dicha coincidencia
# Exactamente, esta busca el elemento y no el índice
# comprado2 =no_olvidar.remove("huevos")
# print(no_olvidar)


# Funciones útiles sobre listas.
# len(lista) Esta función recibe una lista como parámetro y nos retorna la longitud de dicha lista(la cantidad de elementos dentro de esa lista)

# print(len(no_olvidar))

# Para saber si un elemento está o no dentro de una lista, utilizamos un operador in, este entregará como resultado un valor booleano.
# elemento in lista
# print("lechuga" in no_olvidar)

# PAra buscar la posición de un elemento, hay que utilizar el método index()
# lista.index(elemento)
# print(no_olvidar.index("lechuga"))

# Pasar de un str a list.
# texto = input("ingresa una lista: ")
# no_olvidar= []
# inicio = 0
# for i in range(0,len(texto)):
#     if texto[i] == ",":
#         no_olvidar.append(texto[inicio:i])
#         inicio = i+1
# no_olvidar.append(texto[inicio:])
# # print(no_olvidar)

# Esto se puede hacer mucho más simple: 
# Con el metodo split, este es un metodo str y no list, pero nos permite separar un string cada vez que ocurra un texto que le llamamos separador, y así obtener como resultado una lista con todos los elementos separados de acuerdo al separador
# string.split(separador)
# texto = input("ingresa una lista: ")
# no_olvidar = texto.split(",")
# print(no_olvidar)

# Para ordernar una lista, utilizamos el método sort()
# list.sort()
# no_olvidar.sort()


# Ultimos ejercicios

def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista) / len(lista)
    total = 0.0
    for i in lista:
        total += (i - x) ** 2
        y = total / len(lista)
    y= round(y**(1/2),3)
    return x,y
 
lista = [76, 17, 66, 52, 87, 76, 82, 23, 45, 14, 17, 25, 42, 32, 77, 57]
print(promedio_std(lista))
lista = [33, 13, 73, 68, 80, 100, 18, 24, 55, 6, 4]
print(promedio_std(lista))



# Este esta mal ya que me da el nombre del color como un array
def color_frecuente(lista):
    contador = {}
    for color in lista:
        if color in contador:
            contador[color] += 1 
        else:
            contador[color] = 1
    m = max(contador.values()) 
    color_seleccionadoA = [key for key, value in contador.items() if value == m]
    color_seleccionado = "".join(color_seleccionadoA)
    return color_seleccionado, m
# cuidando el retorno, nombre y argumentos

colores = ['azul', 'rojo', 'verde', 'rojo', 'rojo', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo']

print(color_frecuente(colores))
