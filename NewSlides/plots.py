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

plt.clf()
x = np.linspace(-5.0, 5.0, 1001)
p = np.exp(-0.5*x**2)/np.sqrt(2.0*np.pi)
plt.plot(x, p)
plt.ylim(0.0)
plt.xlabel("$x$")
plt.ylabel("Probability Density")
plt.title("A continuous probability distribution")
plt.savefig("images/normal.pdf", bbox_inches="tight")

plt.plot([1.0, 1.0], [0.0, np.exp(-0.5*1.0**2)/np.sqrt(2.0*np.pi)],
         color="r")
plt.plot([2.0, 2.0], [0.0, np.exp(-0.5*2.0**2)/np.sqrt(2.0*np.pi)],
         color="r")

subset = (x > 1.0) & (x < 2.0)
plt.fill_between(x[subset],
                 y1=np.zeros(len(x[subset])), y2=p[subset], color="r", alpha=0.3)
plt.savefig("images/integral.pdf", bbox_inches="tight")

