puzzle = '''
915342678
683197245
427568931
871926354
349851762
256473819
764219583
598734126
132685497
'''

# matrix = [
#     [9, 1, 5, 3, 4, 2, 6, 7, 8], 
#     [6, 8, 3, 1, 9, 7, 2, 4, 5], 
#     [4, 2, 7, 5, 6, 8, 9, 3, 1], 
#     [8, 7, 1, 9, 2, 6, 3, 5, 4], 
#     [3, 4, 9, 8, 5, 1, 7, 6, 2], 
#     [2, 5, 6, 4, 7, 3, 8, 1, 9], 
#     [7, 6, 4, 2, 1, 9, 5, 8, 3], 
#     [5, 9, 8, 7, 3, 4, 1, 2, 6], 
#     [1, 3, 2, 6, 8, 5, 4, 9, 7]
# ]

# convert string representation to "matrix" (nested lists)
matrix = puzzle.strip().split()
# print(rows)

# break up each of the string based numbers into number lists
for n in range(len(matrix)):
    matrix[n] = list(matrix[n])
    # print(matrix[n])
    
    for index, value in enumerate(matrix[n]):
        matrix[n][index] = int(value)
        
    # print(matrix[n])
    
# r is storing the row number
# row is storing the current row we are looking at
for r, row in enumerate(matrix):
    # c is the current column number
    # col is the reference to the actual column value
    # the inner loop is processing the columns from each row
    for c, col in enumerate(row):
        print(col, end=' ')
        if c % 3 == 2 and c < 8:
            print('|', end=' ')
    print()
    if r % 3 == 2 and r < 8:
        print('------+-------+------')
        
# validate rows
valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for r, row in enumerate(matrix):
    if sorted(row) == valid:
        print(f'Row {r} is valid.')
    else:
        print(f'Row {r} is invalid.')
        
# validate columns
for column_number in range(9):
    column = []
    for row in matrix:
        column.append(row[column_number])
    # print(column)
    if sorted(column) == valid:
        print(f'Column {column_number} is valid.')
    else:
        print(f'Column {column_number} is invalid.')
        
# Validate grids
'''
We use two outer loops (grid_row and grid_col) to iterate over the starting positions 
of each 3x3 grid. These loops increment by 3 each time.
For each 3x3 grid, we use two inner loops to iterate over the cells within that grid.
We append each cell value to a grid list.
After collecting all 9 values for a grid, we append that grid list to our grids list.
'''
grids = []
for grid_row in range(0, 9, 3):
    for grid_col in range(0, 9, 3):
        grid = []
        for row in range(grid_row, grid_row + 3):
            for col in range(grid_col, grid_col + 3):
                grid.append(matrix[row][col])
        grids.append(grid)

for i, grid in enumerate(grids):
    # print("Grid", i, grid)
    if sorted(grid) == valid:
        print(f'Grid {i} is valid.')
    else:
        print(f'Grid {i} is invalid.')



'''
9 1 5 | 3 4 2 | 6 7 8 
6 8 3 | 1 9 7 | 2 4 5 
4 2 7 | 5 6 8 | 9 3 1 
------+-------+------
8 7 1 | 9 2 6 | 3 5 4 
3 4 9 | 8 5 1 | 7 6 2 
2 5 6 | 4 7 3 | 8 1 9 
------+-------+------
7 6 4 | 2 1 9 | 5 8 3 
5 9 8 | 7 3 4 | 1 2 6 
1 3 2 | 6 8 5 | 4 9 7 
'''

# insert my puzzle
# - use a docstring
# - directly create the data structure a list of lists

# print the puzzle (display to the screen)

# validate the puzzle
# can we validate the rows?
# can we validate the columns?
# can we validate the grid sections?