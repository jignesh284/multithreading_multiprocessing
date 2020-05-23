import concurrent.futures
import time


########## Newer Implementation fo thread  from [Python 3.2] ############

start = time.perf_counter()

def do_something( seconds ):
    print(f"sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f'Done Sleeping... {seconds}'
'''
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = []
    f1 =  executor.submit(do_something, 1)
    f2 =  executor.submit(do_something, 1)
    print(f1.result)
    print(f2.result)
'''

# implemntaion using python map
'''
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]
    
    # here we don't wait for all the threads we ruturn the thread who is done executing
    for f in concurrent.futures.as_completed(results):
        print(f.result()) 
'''

# implemntaion using python map
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs) 
    
    # here we wait for all the results before printing
    for result in results:
        print(result) 


    

# this will be executed after both the threads are done execution
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')