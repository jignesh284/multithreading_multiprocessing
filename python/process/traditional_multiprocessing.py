 # Example of Multiprocessing in python

#######
# threading is benificial when they are input output bound task 
# on the other hand the task which are cpu bound then the threading is not that beneficial
# Threading is just the illusion of running code concurrently 
#######

########## Older Implementation for porcessing ############

import multiprocessing
import time
start = time.perf_counter()

def do_something( seconds ):
    print(f"sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print('Done Sleeping...')

'''
# do something
p1 = multiprocessing.Process(target=do_something, args=[1])
p2 = multiprocessing.Process(target=do_something, args=[1])

# start the process
p1.start()
p2.start()

# start the process
p1.join()
p2.join()
'''

# multiple loops

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

# this will be executed after both the threads are done execution
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')


