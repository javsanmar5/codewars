def determinant(matrix: list) -> int:
    return determinant_rec(matrix, 0)

def determinant_rec(matrix: list, acum: int) -> int:
    if len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 2:
        acum = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        pass