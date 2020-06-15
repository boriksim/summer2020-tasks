# 2020-06-15
# Quicksort
import random
import time
from my_lib import bubble_sort, quick_sort

rand_list = []
for j in range(10000):
    rand_list.append(random.randint(0, 1000))

t1 = time.time()
# print(bubble_sort(rand_list))
print(quick_sort(rand_list))
t2 = time.time()
print(t2 - t1)
