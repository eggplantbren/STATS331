# Load the rjags library
library('rjags')

# Load my make_list function
source('../make_list.r')

set.seed(1234)

# Load data from file
data = source('data.txt')$value

# Create a model
m = jags.model(file='model.txt', data=data)

# Burn-in
update(m, 10000)

# Do the MCMC for real
draw = jags.samples(m, 5000, thin=10, variable.names = c('beta0', 'beta1', 'sigma'))

# Convert to a list
results = make_list(draw)

# Save as a text file
chains = array(NA, dim=c(500, 3))
chains[,1] = draw$beta0
chains[,2] = draw$beta1
chains[,3] = draw$sigma
write.table(chains, 'chains.txt', row.names=FALSE, col.names=FALSE)

