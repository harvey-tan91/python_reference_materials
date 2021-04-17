#%%
import statistics
import random

#%%
lst = [random.randint(1,1000) for _ in range(10000)]

x1 = statistics.mean(lst)
x2 = statistics.median(lst)
x3 = statistics.geometric_mean(lst)
x4 = statistics.harmonic_mean(lst)
x5 = statistics.stdev(lst) # sample standard deviation
x6 = statistics.variance(lst) # sample variance
x7 = statistics.pstdev(lst) # population standard deviation
x8 =  statistics.pvariance(lst) # population variance
