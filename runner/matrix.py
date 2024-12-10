import sympy as sp

def matrixPrint(matrix):
    s = ''
    for i in matrix:
        for j in i:
            s += f'{j}       '.replace('•sqrt(', '√').replace(')', '')
        s += '\n'
    return f'\n\n{s}\n\n'

def matrixTrans(matrixInp):
    rows = matrixInp.split('?')
    matrix = sp.Matrix([[sp.sympify(cell, rational=True) for cell in row.split()] for row in rows])
    if matrix.rows != matrix.cols:
        raise ValueError("Матрица должна быть квадратной.")
    det = matrix.det()
    if det == 0:
        raise ValueError("Матрица необратима (определитель равен 0).")
    inverse = matrix.inv()
    inverse_as_strings = [[str(cell) for cell in row] for row in inverse.tolist()]
    for i in range(0, len(inverse_as_strings)):
        inverse_as_strings[i] = list(map(lambda g: g.replace("*", "•"), inverse_as_strings[i]))
    return inverse_as_strings