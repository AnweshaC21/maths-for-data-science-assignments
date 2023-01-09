from scipy import linalg
import numpy as np

# b. Perform LU decomposition for square matrix

A = np.loadtxt(open('Matrix_A.csv'), delimiter=',')
print(f'A = {A}')
P, L, U = linalg.lu(A)
print(f'\nLower triangular matrix, L = \n{L}')
print(f'\nUpper triangular matrix, U = \n{U}')
