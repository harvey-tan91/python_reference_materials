
"""
WALRUS OPERATOR
===============
 
"""
#%%

for x in range(10):
    if (term := x) > 5:
        print(term)

print()

for x in range(10):
    if term := x > 5:
        print(term)



#%%
sample_data = [ 
    {"userId": 1,  "name": "rahul", "completed": False}, 
    {"userId": 1, "name": "rohit", "completed": False}, 
    {"userId": 1,  "name": "ram", "completed": False}, 
    {"userId": 1,  "name": "ravan", "completed": True} 
] 
#old method
for entry in sample_data:
    name = entry.get('name')
    if name: # this try to evaluate if it is true
        print(name)

# %%
# new method
for entry in sample_data:
    if name := entry.get('name'):
        print(name)


# %%
