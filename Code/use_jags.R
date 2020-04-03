model = "model
{
  theta ~ dunif(0, 1)
  x ~ dbin(theta, N)
}
"

# The data (use NA for no data)
data = list(x=2, N=5)

# Variables to monitor
variable_names = c("theta", "x")

# How many burn-in steps?
burn_in = 1000

# How many proper steps?
steps = 100000

# Thinning?
thin = 10

# Random number seed
seed = 42

library("rjags")

# Write model out to file
fileConn=file("model_temp.txt")
writeLines(model, fileConn)
close(fileConn)

# Create a JAGS model object
jm = jags.model("model_temp.txt", data)

# Do some burn-in
update(jm, burn_in)

# Do some MCMC
results = jags.samples(jm, variable_names, steps, thin)

# Plot a trace plot
plot(as.vector(results$theta), type="l")