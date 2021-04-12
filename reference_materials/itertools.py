"""
FUNCTIONS
=========
itertools.zip_longest 






"""






#%%
import itertools 

small_list = [i for i in range(5)]
small_list_new = [i for i in range(100,105)]
big_list = [i for i in range(1000,1010)]

print(list(zip(small_list, big_list)))
print(list(itertools.zip_longest(small_list, big_list)))
# zip_longest will iterate through the longer list
# zip will iterate up to the shorter list

#%%
dice1 = [i for i in range(1,7)]
dice2 = [i for i in range(1,7)]

x = list(itertools.product(dice1, dice2))
print(f'Number of possible combinations: {len(x)}')
print(x)
# %%
color = ['red', 'blue', 'green', 'yellow']
x = list(itertools.permutations(color, 3))
# the order of the items matter where (1,2) != (2,1) and count = 2
print(f'Number of possible permutation: {len(x)}')
x
# %%
y = list(itertools.combinations(color, 3))
# the order of the items does not matter where (1,2) == (2,1) and count = 1
print(f'Number of possible combinations: {len(y)}')
y
# %%
lst = [1,5,3,4,5]
print(list(itertools.accumulate(lst)))
print(list(itertools.accumulate(lst, func=max)))
#%%
lst = ['apple', 'apple', 'orange', 'pear', 'pear']
list(itertools.groupby(lst))

#%%
lol_1 = [['apple', 'apple'], ['orange', 'orange'], ['pear', 'pear']]
lol_2 = [['apple', 'apple'], 'orange', ['pear', 'pear']]
print(list(itertools.chain.from_iterable(lol_1)))
print(list(itertools.chain.from_iterable(lol_2)))

# %%
