# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack','Monrroy','Arlette','Palestina'] 

def random_function(students):
    first = students[0] # 0(1)
    total = 0 # o(1)
    new_list = [] # O(1)

    for student in students:
        print ("Se le suma 1 a total")
        total += 1 # O(n)
        new_list.append(student) # O(n)

    print ("Imorimindo estudiantes")
    print(new_list) # O(1)
    return total # O(1)

print (f"Tamano de lista; {len(student_list_01)}")
print(random_function(student_list_01))
print ("")

# Calcular O(?)
"""
O(2n + 5) = O(n)
"""