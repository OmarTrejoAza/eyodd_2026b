"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100 
"""

#Importarmos biblioteca time
import time

# Tomando el timempo inicial
timestamp_01 = time.time ()

#Programa que calcula las sumas
# de los "n" numeros naturales

n = 4000
total_sum = 0

# Ciclo for
for number in range(1, n+1):
    print(number, end=",")
print ("")

print ("")
print ("")
print ("")

# Ciclo for pero en suma 
for number1 in range(1, n+1):
    total_sum = total_sum + number1
    """
    1: sum <- 0 + 1
    sum = 1
    2: sum <- 1 + 2
    sum = 3
    3: sum <- 3 + 3
    sum = 6
    ...
    100: sum <- antSum + 100
    """
print (f"La suma de 1 hasta {n} es: {total_sum}")
# f = formal formato, f string 

print ("")
print ("")
print ("")

#Tomando el timepo final 
timestamp_02 = time.time ()

#Impresion del tiempo de ejecuciom
print(f"tiempo de ejecucion: {(timestamp_02 - timestamp_01) * 1e6:.2f} µs")

"""
  n  |   µ
-----|------
100  | 354.53 µs
500  | 1116.28 µs
1000 | 2612.11 µs
1500 | 3758.67 µs
2000 | 3800.63 µs
2500 | 5127.19 µs
3000 | 7767.20 µs
3500 | 7606.74 µs
4000 | 8218.77 µs

"""