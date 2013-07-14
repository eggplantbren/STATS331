# Load the rjags library
library('rjags')

set.seed(1234)

# Load my make_list function
source('../make_list.r')

# Load fake data from file
data = source('starling_data.txt')$value
boxplot(data$y[data$group==1], data$y[data$group==2], data$y[data$group==3], data$y[data$group==4],
				xlab='Location', ylab='Mass (grams)', main='Starling Data',
				names=c(1, 2, 3, 4))
# Create a model
m = jags.model(file='model.txt', data=data)

# Burn-in
update(m, 10000)

# Do the MCMC for real
draw = jags.samples(m, 100000, thin=10,
		variable.names = c('mu', 'sigma',
			'grand_mean', 'log_diversity'))

# Convert to a list
results = make_list(draw)

# Plot (samples from) the posterior distribution for sigma
hist(results$sigma, breaks=100, xlab='Sigma', ylab='Number')

chains = array(NA, dim=c(10000, 7))
chains[,1:4] = results$mu
chains[,5] = results$sigma
chains[,6] = results$grand_mean
chains[,7] = results$log_diversity
write.table(chains, 'chains.txt', row.names=FALSE, col.names=FALSE)

