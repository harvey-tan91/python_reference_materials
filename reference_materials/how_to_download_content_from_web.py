#%%
from pandas.io import json
import requests
from pandas import json_normalize

content = requests.get(r'http://pythonscraping.com/pages/page1.html') # this return a Response object
print(content.text) # this return a string obj
print(content.content) # this return the result in bytes datatype
print()

print(content.status_code) # refer to < https://en.wikipedia.org/wiki/List_of_HTTP_status_codes > 
print(content.encoding)
print(content.headers) 

#%%
json_content = requests.get(r'https://www.tablebuilder.singstat.gov.sg/publicfacing/api/json/title/15694.json')
json_content = json_content.json()
json_normalize(json_content)
#%%
json_normalize(json_content, 'Level1')

