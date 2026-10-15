from array import array as arr

# Importando una funcion de otro 
# Archivo
from s02t0102_1d import print_array

my_array = arr('i',[2,10,15,20,10])

print ("--- ANTES DE LA ElIMINACION ---")
print_array (my_array)

# Eliminacion
my_array.remove(10)
print ("--- DESPUES DE LA ELIMINACION ---")
print_array (my_array)

#Si ay un errir
try:
    Print("--- DESPUES DE LA ELIMINACION ---")
    my_array.remove(100)
except:
    print("No se encuentra en el arreglo")
print_array(my_array)


