from pylab import *

rc("font", size=16, family="serif", serif="Computer Sans")
rc("text", usetex=True)

x = linspace(-2, 2, 1001)

plot(x, x**2, 'b', linewidth=2, label='Quadratic')
plot(x, abs(x), 'r', linewidth=2, label='Linear')
plot(x, abs(x) < 0.05, 'g', linewidth=2, label='All-or-nothing')
ylim([-0.1, 4])
xlabel('$\hat{\\theta} - \\theta$', fontsize=20)
title('Three Loss Functions')
legend(loc='upper center')
ylabel('Loss (badness) (negative of utility)')
#savefig('utility.pdf', bbox_inches='tight')
show()


