# Load the rjags library
library('rjags')

# Load my make_list function
source('../make_list.r')

# Load data from file
source('data.txt')

# Create a model
m = jags.model(file='model1.txt', data=data)

# Burn-in
update(m, 10000)

# Do the MCMC for real
draw = jags.samples(m, 100000, thin=10,
		variable.names = c('mu1', 'mu2', 'sigma'))

# Convert to a list
results = make_list(draw)

# Plot (samples from) the posterior distribution for sigma
hist(results$sigma, breaks=100, xlab='Sigma', ylab='Number')

# Probability of H0
print(mean(abs(results$mu1 - results$mu2) < 1E-6))
plot(results$mu1, results$mu2, cex=0.1)

