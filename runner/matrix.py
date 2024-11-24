from numpy import linalg, array
from fractions import Fraction

def matrixTrans(matr) :
    matrix = array(matr)
    try:
        inverseMatrix = linalg.inv(matrix)
        inverse = inverseMatrix.tolist()
        inverseMatrixAsFractions = array([[Fraction(str(element)).limit_denominator() for element in row] for row in inverse])
        inversedMatrix = []
        for row in inverseMatrixAsFractions:
            inversedMatrix.append([str(element) for element in row])
    except linalg.LinAlgError:
        return 0
    newMatrix = [[0 for i in range(len(matr))] for i in range(len(matr))]
    for i in range(len(matr)):
        for j in range(len(matr)):
            newMatrix[i][j] = inversedMatrix[j][i]
    return newMatrix