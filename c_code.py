import numpy as np

# c. Solve the equation Ax=b and check whether there are 0,1 or infinitely many solutions

A = np.loadtxt(open('Matrix_A.csv'), delimiter=',')
b = np.loadtxt(open('Vector_b.csv'), delimiter=',')
print(f'A = {A}')
print(f'b = {b}\n')

rank_A = np.linalg.matrix_rank(A)
rank_aug = np.linalg.matrix_rank(np.column_stack((A,b)))

if rank_A < rank_aug:
    print('No solutions exist')
elif rank_A == rank_aug and rank_aug < A.shape[0]:
    print('Infinite solutions exist')
elif rank_A == rank_aug and rank_aug == A.shape[0]:
    print('Unique solution exists')
    x = np.linalg.inv(A).dot(b)
    print(f'The solution of Ax=b is, x = \n{x}')
