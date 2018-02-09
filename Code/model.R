# A dataset
# This could easily be loaded from an external file
data = list(t=c(1,   2,  3,  4,  5,  6,  7,  8,  9, 10),
            y=c(21, 19, 23, 40, 27, 22, 31, 39, 28, 42),
            N=10)

# Prior widths for each parameter (these help set scale for proposal)
widths = c(10, 1)

# Function for the prior distribution
# Input: parameter vector
# Output: log of the probability density
log_prior = function(params)
{
    logp = 0

    # A Normal(0, sd=10) prior for the first parameter
    logp = logp + dnorm(params["log_lambda0"], 0, 10, log=TRUE)

    # A Normal(0, 1) prior for the second parameter
    logp = logp + dnorm(params["slope"], 0, 1, log=TRUE)

    return(logp)
}

# Log likelihood function
# Input: parameter vector
# Output: log likelihood value
log_likelihood = function(params)
{
    # Calculate poisson rate as a function of time
    lambda = exp(params["log_lambda0"] + params["slope"]*data$t)

    # Poisson likelihood
    logl = sum(dpois(data$y, lambda, log=TRUE))

    return(logl)
}

# Proposal distribution
proposal = function(params)
{
    # Copy the parameters
    params2 = params

    # Which parameter to change?
    i = sample(1:length(params), 1)

    # Step size - Brendon's favourite magic
    step_size = widths[i]*10^(1.5 - 3*abs(rt(1, df=2)))

    params2[i] = params2[i] + step_size*rnorm(1)
    return(params2)
}

