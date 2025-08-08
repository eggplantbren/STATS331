import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

rng.seed(0)

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


plt.close("all")
plt.figure(figsize=(10, 8))
x = np.arange(2)
prior = np.array([0.5, 0.5])

for i in range(9):
    plt.subplot(3, 3, i+1)
    lik = np.array([1.0, 0.5**i])
    h = prior*lik
    Z = np.sum(h)
    post = h/Z

    plt.bar(x, post, width=0.3)
    plt.xlim([-1, 2])
    plt.xticks([])
    plt.yticks([])
    plt.title(str(i))
plt.savefig("images/two_balls_updating.pdf", bbox_inches="tight")


plt.close("all")
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
x = np.linspace(0.0, 20.0, 51)
p = np.exp(-0.5*(x - 10.0)**2/3.0**2)
p = p/np.sum(p)
plt.bar(x, p, width=0.3)
plt.ylabel("Probability")
plt.title("Prior Distribution $p(\\theta)$")

plt.subplot(2, 1, 2)
p = np.exp(-0.5*(x - 8.0)**2/0.9**2)
p = p/np.sum(p)
plt.bar(x, p, width=0.3)
plt.title("Posterior Distribution $p(\\theta \\,|\\, x)$")
plt.xlabel("Possible parameter value $\\theta$")
plt.ylabel("Probability")
plt.savefig("images/updating.pdf", bbox_inches="tight")

plt.close("all")
x = np.linspace(0.0, 1.0, 11)
p = x**6*(1.0 - x)**4
p = p/np.sum(p)
plt.bar(x, p, width=0.03)
plt.xlabel("Parameter $\\theta$")
plt.ylabel("Probability $p(\\theta \\,|\\, x)$")
plt.title("Posterior Distribution")
plt.savefig("images/election.pdf", bbox_inches="tight")


plt.close("all")
lamb = np.linspace(0.1, 100.0, 1000)
p1 = lamb**20*np.exp(-lamb)
p1 = p1/np.sum(p1)
p2 = lamb**19*np.exp(-lamb)
p2 = p2/np.sum(p2)
plt.plot(lamb, p1, label="Uniform Prior")
plt.plot(lamb, p2, label="Log-uniform Prior")
plt.legend()
plt.xlabel("Parameter $\\lambda$")
plt.ylabel("Probability $p(\\lambda \\,|\\, x)$")
plt.ylim(0.0)
plt.savefig("images/volcano_posterior_comparison.pdf", bbox_inches="tight")

plt.close("all")
theta = np.linspace(0.0, 1.0, 1001)
p = theta**6*(1.0 - theta)**4
p = p/np.trapz(p, x=theta)
plt.plot(theta, p)
plt.ylim(0.0)
plt.xlabel("$\\theta$")
plt.ylabel("$p(\\theta \\,|\\, x)$")
plt.savefig("images/beta_posterior.pdf")

plt.close("all")
lamb = np.linspace(0.0, 20.0, 1001)
p = lamb**(15 - 1)*np.exp(-3*lamb)
p = p/np.trapz(p, x=lamb)
plt.plot(lamb, p)
plt.ylim(0.0)
plt.xlabel("$\\lambda$")
plt.ylabel("$p(\\lambda \\,|\\, x_1, x_2, x_3)$")
plt.savefig("images/gamma_posterior.pdf")


plt.close("all")
theta = np.linspace(0.0, 1.0, 1001)
p = theta**6*(1.0 - theta)**4
p = p/np.trapz(p, x=theta)
plt.plot(theta, p)
plt.plot([7/12, 7/12], [0.0, 3.0], label="Posterior Mean")
plt.plot([6/10, 6/10], [0.0, 3.0], label="Posterior Mode")
plt.plot([(7-1/3)/(7+5-2/3), (7-1/3)/(7+5-2/3)], [0.0, 3.0], label="Posterior Median")
plt.xlabel("$\\theta$")
plt.ylabel("$p(\\theta \\,|\\, x)$")
plt.legend()
plt.ylim([0.0, 3.0])
plt.savefig("images/point_estimates.pdf")


plt.close("all")
x = np.linspace(-5.0, 5.0, 1001)
plt.plot(x, x**2, label="Quadratic Loss")
plt.plot(x, np.abs(x), label="Absolute Loss")
y = np.ones(len(x))
y[np.abs(x) < 0.1] = 0.0
plt.plot(x, y, label="All-or-Nothing Loss")
plt.ylim(0.0)
plt.legend()
plt.xlabel("$\\hat{\\theta} - \\theta$")
plt.ylabel("Loss")
plt.title("Three Loss Functions")
plt.savefig("images/loss_functions.pdf")


plt.close("all")
x = np.linspace(0.0, 20.0, 1001)
for theta in [7.0, 10.0, 13.0]:
    p = np.exp(-x)
    p[x <= theta] = 0.0
    p /= np.trapz(p, x=x)
    plt.plot(x, p, label=f"$\\theta = {theta}$")
plt.legend()
plt.ylim(0.0)
plt.xlabel("Lifetime $x$")
plt.ylabel("Probability Density")
plt.savefig("images/shifted_exponential.pdf")

plt.close("all")
plt.figure(figsize=(8, 9))
x = np.linspace(-10.0, 10.0, 101)
p = np.exp(-0.5*(x - 3)**2/2**2)
p = p/np.sum(p)
plt.subplot(2, 1, 1)
plt.bar(x, p)
plt.ylim(0.0)
plt.ylabel("Probability")
plt.title("Using a Grid: This is a bar plot.")
plt.subplot(2, 1, 2)
x = 3.0 + 2.0*rng.randn(1000)
plt.hist(x, bins=30)
plt.xlim([-10.0, 10.0])
plt.title("Using Samples: This is a histogram.")
plt.ylabel("Number of Samples")
plt.xlabel("A Parameter $\\theta$")
plt.savefig("images/grid_vs_samples.pdf")

plt.close("all")
x = rng.randn()
keep = []
for i in range(300):
    keep.append(x)
    y = x + 3*rng.randn()
    if rng.rand() <= np.exp(-0.5*y**2 + 0.5*x**2):
        x = y
plt.plot(keep)
plt.xlabel("Iteration")
plt.ylabel("Position $\\theta$")
plt.savefig("images/metropolis.pdf")

plt.close("all")
data = np.loadtxt("../Data/road.txt")
plt.plot(data[:,0], data[:,1], "o", alpha=0.3)
plt.xlabel("$x$ (Age in years)")
plt.ylabel("$y$ (Distance in feet)")
plt.xlim([0, 100])
plt.ylim([0, 800])
plt.title("Road Data")
plt.savefig("images/road_data.pdf")

plt.close("all")
data = np.loadtxt("../Data/outlier.txt")
plt.plot(data[:,0], data[:,1], "o", alpha=0.3)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Outlier Data")
plt.savefig("images/outlier_data.pdf")

plt.close("all")
data = np.loadtxt("../Data/chd.data", skiprows=1)
plt.plot(data[:,0], data[:,1], "o", alpha=0.3)
plt.xlabel("Age (years)")
plt.ylabel("Heart Disease Status")
plt.savefig("images/chd_data.pdf")

