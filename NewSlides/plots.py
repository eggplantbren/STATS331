import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.size": 14,
})


# Geometric distribution plot
x = np.arange(11)
p = 0.7**x
p = p/np.sum(p)

plt.bar(x, p)
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.title("A discrete probability distribution")
plt.savefig("images/geometric.pdf", bbox_inches="tight")
