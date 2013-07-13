# Load the rjags library
library('rjags')

# Load my make_list function
source('../make_list.r')

# Load data from file
source('data.txt')

# Run model 1 and save results
m = jags.model(file='model1.txt', data=data)
update(m, 10000)
draw = jags.samples(m, 100000, thin=100,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(1000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='chains1.txt', row.names=FALSE, col.names=FALSE)

# Run model 2 and save results
m = jags.model(file='model2.txt', data=data)
update(m, 10000)
draw = jags.samples(m, 100000, thin=100,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(1000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='chains2.txt', row.names=FALSE, col.names=FALSE)

# Run model 3 and save results
m = jags.model(file='model3.txt', data=data)
update(m, 10000)
draw = jags.samples(m, 100000, thin=100,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(1000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='chains3.txt', row.names=FALSE, col.names=FALSE)

