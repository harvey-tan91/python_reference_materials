#%%
import collections
import random

lst = [random.randint(1,5) for _ in range(500)]
lst_counter = collections.Counter(lst)

print(lst_counter)
print(lst_counter.keys())
print(lst_counter.values())
print(lst_counter.items())
print(lst_counter.most_common())

