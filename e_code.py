import numpy as np

# e. Give exponential, sine and sigmoid functions on A

A = np.loadtxt(open('Matrix_A.csv'), delimiter=',')
print(f'A = {A}')

# Exponential function
print(f'\nExp(A) = {np.exp(A)}')

# Sine function
print(f'\nSin(A) = {np.sin(A)}')


# Sigmoid function
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


print(f'\nSigmoid(A) = {sigmoid(A)}')
