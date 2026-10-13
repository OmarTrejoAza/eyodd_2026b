#Array
#from array import 
import array as arr

# Creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble
# u: Caracteres unicode
my_array = arr.array('i',[10,20,300,3,7,
40,55,80,700,654,34])

#Interaccion automatica
"""
for num in my_array:
    print(num)
"""

#Accerso indivial a los elementos
"""
print(my_array[0]) #primer elemento 
print(my_array[1]) #segundo elemento 
print(my_array[2]) #tercer elemento 
"""

# Tamano de un arreglo
# length
""""
print (len(my_array))
"""

#Interaccion por indices 
"""
for i in range (len(my_array)):
    print(f"Elemento {i+1}: {my_array[i]}")
"""

""""
for i in range (len(my_array)):
    if my_array[i] % 2 == 0:    
        print(f"Elemento Num {i+1}: {my_array[i]}")
"""
#BUsqueda de un elemento 
num_to_search = 200

# Modificando un valor usando
#backet notation
my_array[7] = 200

try:
    print (f"Localizanod {num_to_search}: {my_array.index(200)}")
except:
    print("⚠️ Numero no econtrado!!!!")

# Asignado valor en un indice que no existe
try:
    my_array[100] = 3 
except:
    print ("⚠️ Inidice no existe!!!")

