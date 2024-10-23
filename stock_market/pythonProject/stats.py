import scipy as sc
import numpy as np

from scipy import stats

data = [
    [2, 1, 1, 3, 1, 2, 3, 3, 3],
    [2, 2, 2, 3, 3, 2, 3, 2, 3],
    [1, 2, 1, 3, 2, 1, 2, 2, 2],
    [1, 1, 1, 2, 2, 3, 3, 2, 3],
    [1, 3, 3, 2, 1, 3, 1, 3, 1],
    [2, 3, 3, 3, 2, 3, 3, 3, 3],
    [1, 1, 1, 3, 3, 3, 2, 3, 2],
    [3, 1, 1, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 3, 3, 1, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 2, 3],
]

data_inverse = [
    [2, 2, 1, 1, 1, 2, 3, 3, 3],
    [2, 2, 2, 3, 3, 2, 3, 2, 3],
    [1, 2, 1, 3, 2, 1, 2, 2, 2],
    [1, 1, 1, 2, 2, 3, 3, 2, 3],
    [1, 3, 3, 2, 1, 3, 1, 3, 1],
    [2, 3, 3, 3, 2, 3, 3, 3, 3],
    [1, 1, 1, 3, 3, 3, 2, 3, 2],
    [3, 1, 1, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 3, 3, 1, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 2, 3],
]

good_ones = []
# print(stats.describe(data))
# list = [[0, 1], [2, 5], [3, 7], [0, 6], [4, 9], [8, 9]]

for i in range(0, len(data)-1):
    for  j in range(0, len(data)-1):
        res = stats.pearsonr(data[i], data[j])

        if res.pvalue < 0.05 and res.pvalue != 0:
            good_ones.append((i+1,j+1, res.statistic, res.pvalue))

#print('\nR = ', res.statistic)
for x in good_ones:
    print(x)
#print('P-value = ', res.pvalue)

#print('\n',stats.t.interval(confidence=0.95, df=len(data[0])-1, loc=np.mean(data[1]), scale=stats.sem(data[1])))


