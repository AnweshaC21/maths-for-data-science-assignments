import numpy as np

# c. Solve the equation Ax=b and check whether there are 0,1 or infinitely many solutions

A = np.loadtxt(open('Matrix_A.csv'), delimiter=',')
b = np.loadtxt(open('Vector_b.csv'), delimiter=',')
print(f'A = {A}')
print(f'b = {b}\n')

if np.linalg.det(A) != 0:
    x = np.linalg.inv(A).dot(b)
    print('Unique solution exists')
    print(f'The solution of Ax=b is, x = \n{x}')
else:
    print('No solution or infinite solutions')

