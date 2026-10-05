"""
Escirbir un programa que calcule
la suma de los "n" numeros naturales.
Por Ejemplo si n= 100
42 usando un cliclo while
"""

#Importar la biblioteca de tiempo
import time

#Crear las variables pata el problema
n = 100
the_sum = 0

#Tomando el tiempo 1
timestamp_01 = time.time()

#Iniciando la suma
while(n > 0 ):
    the_sum = the_sum + n
    n = n - 1
#Tomamos le timepo 2
timestamp_02 = time .time() 

#Imprimimos solucion 
print (f"La suma es {the_sum}")

#Calculando el tiempo
elapsed_time=  round (( timestamp_02 - timestamp_01) * 1e6,2)
print(f"Tiempo de ejecucion: {elapsed_time}us")