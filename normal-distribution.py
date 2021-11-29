from scipy.stats import truncnorm

# define a function to create random variables with normal distribution
# you should enter mean, standard deviation, lowerbound and upperbound as an inputs

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

#------------------------------------------------------------------------------
samples = get_truncated_normal(mean=333.529, sd=9.1402, low=328, upp=354)
samplea.rvs(17)