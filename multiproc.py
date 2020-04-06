# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:02:20 2020

@author: Ritesh
"""

import time
from multiprocessing import Pool

import os
os.cpu_count()

def timer(seconds):
    print('sleeping now')
    time.sleep(seconds)
    print('sleeping over')
    return 1

# start = time.perf_counter()
# timer(1)
# timer(1)
# timer(1)
# timer(1)
# end = time.perf_counter()

# print(f'finished in {round(end-start,2)} seconds')

if __name__ == '__main__':
	start = time.perf_counter()

	numbers = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	p = Pool()
	result = p.map(timer, numbers)

	p.close()
	p.join()
	end = time.perf_counter()

	print(f'finished in {round(end-start,2)} seconds')

