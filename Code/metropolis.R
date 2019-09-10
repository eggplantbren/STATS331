# An "industrial strength" Metropolis implementation
# for STATS 331

# How many steps to take
steps = 100000

# Thinning
thin = 10

# Load functions that are model-specific
source("model.R")

# Starting position in parameter space
params = c(0.5)

# Give the parameters names (OPTIONAL)
names(params) = c("theta")

# Measure how good it is
logp = log_prior(params)
if(is.nan(logp) | is.infinite(logp))
{
    print("Bad initial position!")
    stop()
}
logh = logp + log_likelihood(params)


# Set up 2D array for storage of results
keep = array(NA, dim=c(steps/thin, length(params)))

# Set up 1D array
logl_keep = array(NA, dim=steps/thin)

# Count number of accepted proposals
accepted = 0

# Do Metropolis
for(i in 1:steps)
{
    # Propose to move somewhere else
    params2 = proposal(params)

    # Measure how good it is. Handle any awkward cases of infinity
    # I.e., if the log prior is -infinity, don't even evaluate log likelihood
    logp2 = log_prior(params2)
    if(is.nan(logp2) | is.infinite(logp2))
    {
        logh2 = -Inf
    } else
    {
        logh2 = logp2 + log_likelihood(params2)
    }

    # Log of acceptance probability
    log_alpha = logh2 - logh
    if(log_alpha > 0)
    {
        log_alpha = 0
    }

    # Accept the proposal with probability alpha
    if(runif(1) < exp(log_alpha))
    {
        params = params2
        logh = logh2
        accepted = accepted + 1
    }

    # Store results
    if(i %% thin == 0)
    {
        keep[i/thin, ] = params
        logl_keep[i/thin] = log_likelihood(params)
        cat("Done", i, "iterations.\n")
    }
}

# Print Metropolis acceptance rate
cat("Acceptance rate =", accepted/steps, "\n")

