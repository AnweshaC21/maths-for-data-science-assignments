import numpy as np

# f. Find all the eigenpairs of A

A = np.loadtxt(open('Matrix_A.csv'), delimiter=',')
print(f'A = {A}')

w, v = np.linalg.eig(A)

print(f'\nEigen values of A = \n{w}')
print(f'\nEigen vectors of A = \n{v}')
