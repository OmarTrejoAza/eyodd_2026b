"""
Generatirs

Los generadores son fuciones que puedes
pusar su ejecucion

Cuando se invoca una funcion generadora
devuelve un objeto generador (aka Interador)

El codigo dentro de la funcuin no se ejecuta
de inmediato, solo se copila

La funcion se ejecuta unicamente cuando
interes sobre el generador.

"""

#def my_generator ():
#    return 1 
#    return 2

#print (my_generator())

def my_generator ():
    yield 1
    yield 2
    yield 3
    yield 4

#para el for
    yield 5
    yield 6
    yield 7
    yield 8

#yiend = producir 

#Se invoca funcion generdora
my_iterador = my_generator()

#se itera manual mente sobre el generador
print (next(my_iterador)) #Imprime 1
print (next(my_iterador)) #Imprime 2
print (next(my_iterador)) #IMprime 3
print (next(my_iterador)) #Imprime 4
#print (next(my_iterador)) #Da Error

# Los iteradores se uede iterar con for
for value in my_iterador:
    print(value)    