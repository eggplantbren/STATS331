import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

rng.seed(0)

num = 100

x = 10.0*rng.randn(num)
y = x + 3.0*rng.randn(num)

x[num-1], y[num-1] = -30.0, 30.0
x[num-2], y[num-2] = 30.0, -30.0

data = np.empty((num, 2))
data[:,0] = x
data[:,1] = y
np.savetxt("outlier.txt", data)

plt.plot(x, y, "o")
plt.show()

