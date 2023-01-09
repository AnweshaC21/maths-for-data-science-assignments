import numpy as np

# a. Read a matrix A from a csv file and a vector b from another csv file

A = np.loadtxt(open('Matrix_A.csv'), delimiter=',')
print('The matrix read from csv file is: ')
print(f'A = {A}')

b = np.loadtxt(open('Vector_b.csv'), delimiter=',')
print('\nThe vector read from csv file is: ')
print(f'b = {b}')
