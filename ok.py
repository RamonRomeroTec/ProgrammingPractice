import numpy as np

from numpy.linalg import matrix_power

m1 = [  [0,1,0,0],
        [.75,0,.25,0],
        [0,1/3,0,2/3], 
        [0,0,1,0] ]




a = np.array(m1)
print(a)
print(matrix_power(a, 2) )
print(matrix_power(a, 3) )
print(matrix_power(a, 4) )
print(matrix_power(a, 5) )
print(matrix_power(a, 6) )
print(matrix_power(a, 7) )