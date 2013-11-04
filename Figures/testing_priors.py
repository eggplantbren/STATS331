from pylab import *

rc("font", size=16, family="serif", serif="Computer Sans")
rc("text", usetex=True)

num = 41
mu = linspace(100, 120, num)

prior1 = 0.5/(num-1)*ones(num)
prior1[-1] = 0.5

prior2 = exp(-0.5*((mu - 120.)/5)**2)
prior2[0:(num-1)] *= 0.7/sum(prior2[0:(num-1)])
prior2[-1] = 0.3

prior3 = 1./(1. + ((mu - 120.))**2)
prior3 /= sum(prior3)

plot(mu, prior1, 'bo-', markersize=5, linewidth=2, label='Prior 1')
plot(mu, prior2, 'ro-', markersize=5, linewidth=2, label='Prior 2')
plot(mu, prior3, 'go-', markersize=5, linewidth=2, label='Prior 3')
xlim([99., 121.])
ylim([0., 0.55])
legend(loc='upper left')
xlabel('Parameter $\\mu$')
ylabel('Prior Probability')
title('Three Different Priors')
#savefig('testing_priors.pdf', bbox_inches='tight')
show()

