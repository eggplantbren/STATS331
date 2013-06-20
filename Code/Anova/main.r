# Load the rjags library
library('rjags')

# Load my make_list function
source('../make_list.r')

# Load fake data from file
data = source('data.txt')$value

# Create a model
m = jags.model(file='model.txt', data=data)

# Burn-in
update(m, 10000)

# Do the MCMC for real
draw = jags.samples(m, 100000, thin=10,
		variable.names = c('mu1', 'mu2', 'mu3', 'sigma',
			'grand_mean', 'log_diversity'))

# Convert to a list
results = make_list(draw)

# Plot (samples from) the posterior distribution for sigma
hist(results$sigma, breaks=100, xlab='Sigma', ylab='Number')


