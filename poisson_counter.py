import numpy as np
import matplotlib.pyplot as plt

def poisson_counter(exponent):
    target_number = np.e**(-int(exponent))
    count, currval = 0, 1
    while currval > target_number:
        count += 1
        currval *= np.random.rand()
    return count

p = np.zeros(100)
for i in range(100):
    p[i] = poisson_counter(10)

plt.plot(p)
plt.show()