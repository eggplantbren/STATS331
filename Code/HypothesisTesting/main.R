set.seed(123)

x = rnorm(100)
# Make the mean 115.9
x = x - mean(x) + 115.9

# Parameter values
mu = seq(110, 120)

# Make the testing prior
prior = rep(0.5/10, 11)
prior[11] = 0.5
# Compute the likelihood for the 100 data points.
# The numbers get close to 0, so let's use logs
log_lik = 1
# Use a for loop to loop over all data values
# and multiply the likelihoods
for(i in 1:100)
{
  log_lik = log_lik + dnorm(x[i], mean=mu, sd=15, log=TRUE)
}

# Rescale the likelihood for readability
lik = exp(log_lik - max(log_lik))*1000
#lik = lik/max(lik)*1000

# Calculate the posterior
h = prior*lik
post = h/sum(h)

# The null hypothesis
post[11]

print(post)

