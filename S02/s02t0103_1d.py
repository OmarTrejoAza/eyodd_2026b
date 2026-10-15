from array import array as arr

# Importando una funcion de otro 
# Archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20])

print ("--- ANTES DE LA INSERCION ---")
print_array (my_array)

# Insercion
my_array.insert(1,90)
print ("--- DESPUES DE LA INSERCION ---")
print_array (my_array)

print ("--- DESPUES DE LA APPEND ---")
my_array.apppend(1000)
print_array (my_array)

print ("--- DESPUES DE LA APPEND CON INSERT ---")
my_array.INSERT(90000,len(my_array))
print_array (my_array)