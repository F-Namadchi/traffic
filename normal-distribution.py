from scipy.stats import truncnorm
import scipy.stats as stats
import numpy as np

# define a function to create random variables with normal distribution
# you should enter mean, standard deviation, lowerbound and upperbound as an inputs

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

#------------------------------------------------------------------------------
samples = get_truncated_normal(mean=98.9, sd=111.697, low=40, upp=322)
samples = samples.rvs(5)

N = stats.norm(loc=98.9, scale=111.697)
N = N.random_list(5, [40, 322])

#--------------
#add new