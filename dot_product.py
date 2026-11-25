import numpy as np

def dot_product(array1, array2):
    if isinstance(array1, np.ndarray) and isinstance(array2, np.ndarray):
        if len(array1) == len(array2):
            array_result = array1 * array2
            dot_product = sum(array_result)
            print('The dot product of the two arrays is ' + str(dot_product) + '.')
        else:
            print('Arrays are not of equal length.')
    else:
        print("Arrays are not Numpy N-dimensional arrays.")

array1 = np.random.randint(0, 10, size=10)
array2 = np.random.randint(0, 10, size=10)

dot_product(array1, array2)