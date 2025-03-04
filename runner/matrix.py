import sympy as sp

def matrixPrint(matrix):
    '''A_{m,n} = 
        \begin{pmatrix}
        a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
        a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
        \vdots  & \vdots  & \ddots & \vdots  \\
        a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
        \end{pmatrix}'''
    output1 = r'''\(
(A^{-1})^{T} = 
    \begin{pmatrix}
'''
    output = ''
    for i in matrix:
        for j in i:
            if '•' in j:
                splitted = j.split('•')
                if '/' in splitted[0]:
                    splittedNum = splitted[0].split('/')
                    output+= r'\frac{' + fr'{splittedNum[0]}' + r'}{' + fr'{splittedNum[1]}' + '}' + fr'{splitted[1]} &'
                else:
                    output+= rf'{splitted[0]}' + fr'{splitted[1]} &'.replace('•', '\\')
            else:
                if '/' in j:
                    splittedNum = j.split('/')
                    output+= r'\frac{' + fr'{splittedNum[0]}' + r'}{' + fr'{splittedNum[1]}' + r'} &'
                else:
                    output+= rf'{j} &'
        output = output[:-2] + '\\\\\n'
    output = output[:-3] + r'\end{pmatrix}'
    output = output.replace('sqrt', '\\sqrt').replace('(', '{').replace(')', '}')
    return output1 + output + r'\)' + '<br>'
    

def matrixTrans(matrixInp):
    rows = matrixInp.split('?')
    matrix = sp.Matrix([[sp.sympify(cell, rational=True) for cell in row.split()] for row in rows])
    if matrix.rows != matrix.cols:
        raise ValueError("Матрица должна быть квадратной.")
    det = matrix.det()
    if det == 0:
        raise ValueError("Матрица необратима (определитель равен 0).")
    inverse = matrix.inv()
    inverseMatrix = [[str(cell) for cell in row] for row in inverse.tolist()]
    for i in range(0, len(inverseMatrix)):
        inverseMatrix[i] = list(map(lambda g: g.replace("*", "•"), inverseMatrix[i]))
    transposedInverseMatrix = [[0 for _ in range(len(inverseMatrix))] for _ in range(len(inverseMatrix))]
    for i in range(len(inverseMatrix)):
        for j in range(len(inverseMatrix)):
            transposedInverseMatrix[j][i] = inverseMatrix[i][j]
    return transposedInverseMatrix