# Función para imprimir la cuadrícula del Sudoku
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()

# Función para encontrar una ubicación vacía en la cuadrícula del Sudoku
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):     # Si el valor es 0, la celda está vacía
                l[0]= row              # Actualiza la ubicación de la celda vacía
                l[1]= col
                return True            # Devuelve Verdadero si se encontró una ubicación vacía
    return False                     # Devuelve Falso si no hay ubicaciones vacías

# Función para verificar si un número ya se utiliza en una fila
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True    # Devuelve Verdadero si el número ya se encuentra en la fila
    return False          # Devuelve Falso si el número no se encuentra en la fila

# Función para verificar si un número ya se utiliza en una columna
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True    # Devuelve Verdadero si el número ya se encuentra en la columna
    return False          # Devuelve Falso si el número no se encuentra en la columna

# Función para verificar si un número ya se utiliza en una caja 3x3
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True    # Devuelve Verdadero si el número ya se encuentra en la caja 3x3
    return False          # Devuelve Falso si el número no se encuentra en la caja 3x3

# Función para verificar si una ubicación es segura para colocar un número
def check_location_is_safe(arr, row, col, num):
    return (not used_in_row(arr, row, num) and    # Devuelve Verdadero si el número no se encuentra en la fila
            not used_in_col(arr, col, num) and    # Devuelve Verdadero si el número no se encuentra en la columna
            not used_in_box(arr, row - row % 3, col - col % 3, num))   # Devuelve Verdadero si el número no se encuentra en la caja 3x3

# Función para resolver el Sudoku
def solve_sudoku(arr):
    l =[0, 0]     # Ubicación de la celda vacía
 
    if(not find_empty_location(arr, l)):   # Si no hay ubicaciones vacías, se ha resuelto el Sudoku
        return True
 
    row = l[0]      # Fila de la ubicación vacía
    col = l[1]      # Columna de la ubicación vacía
 
    # Probamos números del 1 al 9 en la ubicación vacía
    for num in range(1, 10):
        if(check_location_is_safe(arr, row, col, num)):
            arr[row][col]= num   # Coloca el número en la celda
 
           
            if(solve_sudoku(arr)):
                return True
            
            
            arr[row][col] = 0
            
          
    return False
 

if __name__=="__main__":
    
    grid =[[0 for x in range(9)]for y in range(9)]
    
   
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
     
    
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No existe solucion")
