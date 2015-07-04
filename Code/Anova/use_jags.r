model = "model
{
	# Hierarchical prior for the means
	# Hyperparameters
	grand_mean ~ dnorm(0, 1/1000^2)
	log_diversity ~ dunif(-10, 10)
	diversity <- exp(log_diversity)

	# Prior for parameters
	for(i in 1:N_groups)
	{
		mu[i] ~ dnorm(grand_mean, pow(diversity, -2))
	}

	# Log-uniform prior for the s.d.
	log_sigma ~ dunif(-10, 10)
	sigma <- exp(log_sigma)

	# Sampling distribution/likelihood
	for(i in 1:N)
	{
		y[i] ~ dnorm(mu[group[i]], pow(sigma, -2))
	}
}
"

# Load fake data from file
data = source('starling_data.txt')$value
boxplot(data$y[data$group==1], data$y[data$group==2], data$y[data$group==3], data$y[data$group==4],
				xlab='Location', ylab='Mass (grams)', main='Starling Data',
				names=c(1, 2, 3, 4))


# Variables to monitor
variable_names = c('mu', 'sigma', 'grand_mean', 'log_diversity')

# How many burn-in steps?
burn_in = 10000

# How many proper steps?
steps = 10000

# Thinning?
thin = 1




# NO NEED TO EDIT PAST HERE!!!
# Just run it all and use the results list.

library('rjags')

# Write model out to file
fileConn=file("model.temp")
writeLines(model, fileConn)
close(fileConn)

if(all(is.na(data)))
{
	m = jags.model(file="model.temp", inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"))
} else
{
	m = jags.model(file="model.temp", data=data, inits=list(.RNG.seed=123, .RNG.name="base::Mersenne-Twister"))
}
update(m, burn_in)
draw = jags.samples(m, steps, thin=thin, variable.names = variable_names)
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
results = make_list(draw)

# Plot (samples from) the posterior distribution for sigma
hist(results$sigma, breaks=100, xlab='Sigma', ylab='Number')

chains = array(NA, dim=c(10000, 7))
chains[,1:4] = results$mu
chains[,5] = results$sigma
chains[,6] = results$grand_mean
chains[,7] = results$log_diversity
write.table(chains, 'chains.txt', row.names=FALSE, col.names=FALSE)

