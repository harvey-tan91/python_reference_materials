#%%
lst_a = [1,2,3]
lst_b = [20,30,40]
lst_c = [[100,200,300], [500,600,700]]

dict_a = {'apple': 5, 'orange': 10, 'pear': 99}
dict_b = {'jackfruit': 100, 'kiwi': 10, 'banana': 99}

#%%
print(
    [i*2 for i in lst_a] # basic list comprehension
    ) 

print(
    [x for row in lst_c for x in row] # unpacking
    )

print(
    [i for i in lst_b if i>20] # basic filtering
    )

print(
    [i for i in lst_b if i>20 and i <40] # multiple filtering conditions
    )

#%%
print(
    [[i*-1 for i in lst] for lst in lst_c] # list of list comprehension
    )

print(
    [i*1000 if i <= 20 else i for i in lst_b] # conditional expression
    )

print(
    [x + y for x, y in zip(lst_a, lst_b)] # adding element-wise from two list
    )
#%%
{key: value*2 for key, value in dict_a.items()} #basic dictionary comprehnsion
#%%
