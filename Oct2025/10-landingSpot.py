def find_landing_spot(matrix):
    #define matrix size
    rows = len(matrix)
    cols = len(matrix[0])
    #trick from chatgpt to be able to "move" and calculate neighbours
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(rows): 
        for j in range(rows):
            #print(matrix[i][j]) #to read all elements of arrays in arrays
            findZero = matrix[i][j]
            if findZero == 0:
                coordZeroTemp = [i,j]
                 
    return matrix

find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]])
