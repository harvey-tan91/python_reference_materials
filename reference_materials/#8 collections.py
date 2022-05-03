#%%
import collections
import random

lst = [random.randint(1,5) for _ in range(500)]
lst_counter = collections.Counter(lst) 
# return key-value pair with key as the item and the value as the number of occurances for the said item

print(lst_counter)
print(lst_counter.keys())
print(lst_counter.values())
print(lst_counter.items())
print(lst_counter.most_common())

#%%
