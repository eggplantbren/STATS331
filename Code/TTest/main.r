# Load the rjags library
library('rjags')

# Convert to a list
make_list <- function(draw)
{
	results = list()
	for(name in names(draw))
	{
		# Extract "chain 1"
		results[[name]] = as.array(draw[[name]][,,1])
		
		# Transpose 2D arrays
		if(length(dim(results[[name]])) == 2)
			results[[name]] = t(results[[name]])
	}
	return(results)
}

# Load data from file
source('data.txt')

# Run model 1 and save results
m = jags.model(file='model1.txt', inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"), data=list(N1=data$N1, N2=data$N2))
update(m, 10000)
draw = jags.samples(m, 50000, thin=10,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(5000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='prior1.txt', row.names=FALSE, col.names=FALSE)

# Run model 2 and save results
m = jags.model(file='model2.txt', inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"), data=list(N1=data$N1, N2=data$N2))
update(m, 10000)
draw = jags.samples(m, 50000, thin=10,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(5000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='prior2.txt', row.names=FALSE, col.names=FALSE)

# Run model 3 and save results
m = jags.model(file='model3.txt', inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"), data=list(N1=data$N1, N2=data$N2))
update(m, 10000)
draw = jags.samples(m, 50000, thin=10,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(5000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='prior3.txt', row.names=FALSE, col.names=FALSE)


# Run model 1 and save results
m = jags.model(file='model1.txt', inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"), data=data)
update(m, 10000)
draw = jags.samples(m, 100000, thin=100,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(1000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='chains1.txt', row.names=FALSE, col.names=FALSE)
print(mean(results$mu1 < results$mu2))
print(mean(results$mu1 == results$mu2))
print(mean(results$mu1 > results$mu2))

# Run model 2 and save results
m = jags.model(file='model2.txt', inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"), data=data)
update(m, 10000)
draw = jags.samples(m, 100000, thin=100,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(1000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='chains2.txt', row.names=FALSE, col.names=FALSE)
print(mean(results$mu1 < results$mu2))
print(mean(results$mu1 == results$mu2))
print(mean(results$mu1 > results$mu2))

# Run model 3 and save results
m = jags.model(file='model3.txt', inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"), data=data)
update(m, 10000)
draw = jags.samples(m, 100000, thin=100,
		variable.names = c('mu1', 'mu2', 'sigma'))
results = make_list(draw)
chains = array(NA, dim=c(1000, 3))
chains[,1] = results$mu1
chains[,2] = results$mu2
chains[,3] = results$sigma
write.table(chains, file='chains3.txt', row.names=FALSE, col.names=FALSE)
print(mean(results$mu1 < results$mu2))
print(mean(results$mu1 == results$mu2))
print(mean(results$mu1 > results$mu2))


