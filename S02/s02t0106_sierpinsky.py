from array import array as arr

# Parametros de mi cuadricula 
rows = 8
columns = 2 * rows - 1

# Creando la reticula 
matrix = []

# Construyendo fel grid
for _ in  range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validadando la construccion del Grind
print (f"Cantidad de filas: {len(matrix)}")
print (f"Canitdad de columnas {len(matrix[0])}")

for row in matrix:
    print (list (row))