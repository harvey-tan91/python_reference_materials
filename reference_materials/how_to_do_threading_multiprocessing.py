#%%
from sys import path_importer_cache
import threading
import concurrent.futures
import time
from timeit import default_timer as timer
import os
import requests

def do_something():
    print('Sleeping for one second')
    time.sleep(1)
    print('Done sleeping')    

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start() # to start the thread
t2.start()

t1.join()
t2.join()
 # when the join method is invoked, the calling thread is blocked till the tread obj on which it is called is terminated
 # this structure ensures that the thread finishes before it went to the rest of the code

#%%
def do_something_cool(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something_cool, 2)  # this execute the function once
    f2 = executor.submit(do_something_cool, 2) # 2 is the parameter that get passed to the function
    # submit method schedules a function to be executed and return a Future object
    # the Future object captures the execution of our function
    ## and allow us to check in on it after it is scheduled

    print(f1.result()) # result method return the return value of the function
    print(f2.result())

#%%
# if we want to run the function multiple times

number_of_iteration = 10

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something_cool, 2) for _ in range(number_of_iteration)]

    for fut_obj in concurrent.futures.as_completed(results):
        # as_completed method return an iterable which contain the results
        print(fut_obj.result())

# %%
# we can use the map function to map the function over a defined iterable

with concurrent.futures.ThreadPoolExecutor() as executor:
    lst = [5,4,3,2,1] # defined iterable
    results = executor.map(do_something_cool, lst)
    # the map method returns the results, in the order that they were started

    for f in results:
        print(f)

# %%
# Example of a real world example of a threading example

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python\image_download_threading')

image_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

def get_image(url):
    image_content = requests.get(url).content
    image_name = f"{url.split('/')[3]}.jpg"

    with open(image_name, 'wb') as f:
        f.write(image_content)
        print(f'{image_name} was downloaded')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_image, image_urls)
