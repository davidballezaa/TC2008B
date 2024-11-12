import numpy as np
import math

vector1 = np.array([0, 1, 0])
vector2 = np.array([1, 0, 0])

mgn1 = math.sqrt(vector1[0]*vector1[0]+vector1[1]*vector1[1]+vector1[2]*vector1[2])
mgn2 = math.sqrt(vector2[0]*vector2[0]+vector2[1]*vector2[1]+vector2[2]*vector2[2])

dotprod = np.dot(vector1, vector2)

print(dotprod)

thetarad = math.acos(dotprod/(mgn1*mgn2))
thetadeg = thetarad*180/math.pi

print(thetadeg)

vector3 = np.array([2, 0, 1])
vector4 = np.array([1, -1, 3])

crossprod = np.cross(vector3, vector4)

print(crossprod)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

transpose_matrix = matrix.T

print("Matrix:", matrix)
print("Transpose:", transpose_matrix)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[1, 3], [0, 1]])

matsum = matrix1 + matrix2
print("Sum:", matsum)

matescal = 2 * matrix1
print("Scalar:", matescal)

matmult = np.dot(matrix1, matrix2)
print("Multiplication:", matmult)

diagonal = [1, 2, 3]
diag_matrix = np.diag(diagonal)
print("Diagonal Matrix:", diag_matrix)