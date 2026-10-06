"""
NOTAS:
1. Identifico el tamano de la entradan"n"
El tamano de la esntrada es el numero
de estudiantes
2. Es ver cuanto crece el numero de
operaciones en mi algoritmo conforme 
crece el tamano de la entrada
Agrego las bigO identificadad
Teniendo en cuneta la Cota superior assintotica
O(n) + O(4) = O(n+4) = O(n)

"""

#Creando una lista de estudiantes
student_list_1 = ['Jordan','Pipen','Curry','Shack']
student_list_2 = ['Mike','Saul','Walter','Jessy']

#Verificando presencia de 
def check_student (input_student, student_list):
    for student in student_list:
        if input_student == student: # O (n)
            print("✔️Estudiante encontrado") #O (1)
            return student # O (1)
    #Si no encuentra al estudiante 
    print ("❌Estudiante no encontrado") # O(1)
    return None # O (1)

#Provando algotitmo 
check_student("Walter", student_list_2) 