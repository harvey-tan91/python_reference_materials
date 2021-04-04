#%%

import sys
from timeit import default_timer as timer

start = timer() ### START OF TIMER ###

long_lst = [i for i in range(0,10000000)]
long_lst_augmented = [i**2 for i in long_lst]

print(sys.getsizeof(long_lst) / 1000000)
print(sys.getsizeof(long_lst_augmented) / 1000000)

end = timer() ### END OF TIMER ###

print(f'Total Time Taken: {end - start:.4}s') 


