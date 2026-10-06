"""
Escirbir un programa que calcule
la suma de los "n" numeros naturales.
Por Ejemplo si n= 100
42 usando un cliclo while
"""
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
"""
# Importar la biblioteca de tiempo
import time

def sum_of_n(n):
    total_sum = 0
    # Sumando los "n" numeros
    # Ciclo while
    while(n > 0):
        # ¡Aquí estaba el error! Estas líneas necesitan estar indentadas
        total_sum = total_sum + n
        n = n - 1
        
    # Retornando el total de la suma 
    return total_sum

# Variable para guardar el dataset
dataset = [] 

# Generando el contenido del Dataset
for repiticion in range(1, 11):
    # ⏱️ Tomo el tiempo 1 (INICIAL)
    timestamp_01 = time.time()
    
    # Sumo los "n" numeros 
    n = repiticion * 500
    result = sum_of_n(n)

    # ⏱️ Tomando el tiempo final 
    timestamp_02 = time.time()

    # Calculando el tiempo en microsegundos
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregar la tripleta de los datos al dataset
    dataset.append((n, elapsed_time, result))

# Imprimir el dataset
for tup in dataset:
    print(tup)