import numpy as np
import statistics 
import scipy.stats as stats

arr = np.array([1,4,4 ,5,7])

mean=np.mean(arr)

print(mean)

med = np.median(arr)
print(med)

print(stats.mode(arr))

print(statistics.variance(arr.tolist()))

print(statistics.stdev(arr.tolist()))