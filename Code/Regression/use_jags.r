model = "model
{
    # Prior for all the parameters
    beta0 ~ dnorm(0, pow(1E3, -2))
    beta1 ~ dnorm(0, pow(1E3, -2))
    log_sigma ~ dunif(-10, 10)
    sigma <- exp(log_sigma)

    # Likelihood
    for(i in 1:N)
    {
        y[i] ~ dnorm(beta0 + beta1*x[i], pow(sigma, -2))
    }

	y_new ~ dnorm(beta0 + beta1*90, pow(sigma, -2))
}
"

# Load data from file
data = source('data.txt')$value

# Variables to monitor
variable_names = c('beta0', 'beta1', 'sigma', 'y_new')

# How many burn-in steps?
burn_in = 10000

# How many proper steps?
steps = 5000

# Thinning?
thin = 10




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
	m = jags.model(file="model.temp", data=data, inits=list(.RNG.seed=42, .RNG.name="base::Mersenne-Twister"))
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


# Save as a text file
chains = array(NA, dim=c(500, 3))
chains[,1] = draw$beta0
chains[,2] = draw$beta1
chains[,3] = draw$sigma
write.table(chains, 'chains.txt', row.names=FALSE, col.names=FALSE)
write.table(results$y_new, 'prediction.txt', row.names=FALSE, col.names=FALSE)

