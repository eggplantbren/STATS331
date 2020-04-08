model = "model
{
    mu ~ dnorm(0, 1/1000^2)
    sigma ~ dgamma(0.001, 0.001)
    for(i in 1:N)
    {
        x[i] ~ dnorm(mu, 1/sigma^2)
    }

    a[1] ~ dunif(1, 5)
    a[2] ~ dunif(3, 4)
}
"

# A dataset
data = list(x = c(0.044103595329532, -0.922186227194728, 0.0960010565013454, 
-1.12828522333698, 1.36291783960003, -2.23065969145022, -0.93027082294735, 
-2.07175801570109, 1.20069146950599, 3.3937627148158), N = 10)

# Variables to monitor
variable_names = c("mu", "sigma", "a")

# How many proper steps?
steps = 100000

# Thinning?
thin = 10

# Import the rjags library
library("rjags")

# Create a JAGS model object
jm = jags.model(textConnection(model), data)

# Do some MCMC
results = coda.samples(jm, variable_names, steps, thin=thin)

# Extract chains as data frame
results = as.data.frame(results[[1]])
