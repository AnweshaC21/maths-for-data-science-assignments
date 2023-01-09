import numpy as np
from sympy import *

# d. Do the diagonalization of a matrix (assume it is symmetric)

S = Matrix([[1, 5, -2], [5, 4, 5], [-2, 5, 1]])
print(f'Symmetric Matrix, S = \n{np.array(S)}')
P, D = S.diagonalize()
print(f'\nP = \n{np.array(P)}')
print(f'\nDiagonal Matrix, D = \n{np.array(D)}')    # Answer

# Verification
print(f'\nP*D*P_inv = \n{np.dot(np.dot(P, D), P.inv())} = A')
