# A dataset could be loaded here

# Prior widths for each parameter (these help set scale for proposal)
widths = c(1)

# Function for the prior distribution
# Input: parameter vector
# Output: log of the probability density
log_prior = function(params)
{
    logp = 0
    logp = dunif(params, 0, 1, log=TRUE)
    return(logp)
}

# Log likelihood function
# Input: parameter vector
# Output: log likelihood value
log_likelihood = function(params)
{
    # More generally this will use a bigger dataset loaded from a file
    logl = 6*log(params[1]) + 4*log(1 - params[1])
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

