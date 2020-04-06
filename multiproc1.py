# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 07:57:30 2020

@author: Ritesh
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:02:20 2020

@author: Ritesh
"""

import time
import multiprocessing 

import os
os.cpu_count()

def timer(seconds):
    print('sleeping now')
    time.sleep(seconds)
    print('sleeping over')

start = time.perf_counter()

for i in range(10):
    timer(1)
end = time.perf_counter()
print(f'finished in {round(end-start,2)} seconds')

if __name__ == '__main__':
    
    
    start = time.perf_counter()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=timer, args=[1])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()
        
        
    end = time.perf_counter()

    print(f'finished in {round(end-start,2)} seconds')