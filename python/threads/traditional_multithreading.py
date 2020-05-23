 # Example of threading python

#######
# threading is benificial when they are input output bound task 
# on the other hand the task which are cpu bound then the threading is not that beneficial
# Threading is just the illusion of running code concurrently 
#######

########## Older Implementation fo thread ############

import threading
import time
start = time.perf_counter()

def do_something( seconds ):
    print(f"sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print('Done Sleeping...')

'''
# creting two threads with some function
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# execting the threads
t1.start()
t2.start()

# join helps to wait for the methods
t1.join()
t2.join()
'''

# creting ten threads with some function
threads = []
for _ in range(10):
    t = threading.Thread(target = do_something, args=[1.5])
    t.start()
    threads.append(t)

# joining threads to wait
for thread in threads:
    thread.join()
     

# this will be executed after both the threads are done execution
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')


