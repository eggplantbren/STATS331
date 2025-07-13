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


plt.close("all")
x = np.arange(31)
p1 = np.exp(-0.5*(x - 15)**2/2**2)
p1 = p1/np.sum(p1)
p2 = np.exp(-0.5*(x - 15)**2/5**2)
p2 = p2/np.sum(p2)

plt.figure(figsize=(8, 9))
plt.subplot(2, 1, 1)
plt.bar(x, p1)
plt.title("Probability Mass Function 1")
plt.ylabel("Probability")

plt.subplot(2, 1, 2)
plt.bar(x, p2)
plt.title("Probability Mass Function 2")
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.savefig("images/two_distributions.pdf", bbox_inches="tight")


plt.close("all")
x = np.arange(2)
p = 0.5*np.ones(2)
plt.bar(x, p, width=0.3)
plt.xticks([0, 1], ["$BB$", "$BW$"])
plt.xlim([-1, 2])
plt.ylabel("Probability")
plt.title("Two Balls Problem: Prior")
plt.savefig("images/two_balls_prior.pdf", bbox_inches="tight")

plt.close("all")
x = np.arange(2)
p = np.array([2/3, 1/3])
plt.bar(x, p, width=0.3)
plt.xticks([0, 1], ["$BB$", "$BW$"])
plt.xlim([-1, 2])
plt.ylabel("Probability")
plt.title("Two Balls Problem: Posterior")
plt.savefig("images/two_balls_posterior.pdf", bbox_inches="tight")

