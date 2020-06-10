# 2020-06-04
# Найти все простые числа от 2 до N
import numpy as np
import time
max = 100000

t1 = time.time()

# for n in range(2, max):
#     for i in range(2, n - 1):
#         if n % i == 0:
#             break
#     else:
#         print(n)

nums = np.zeros(max)
for i in range(2, max):
    if nums[i] == 0:
        print(i)
    for j in range(i, max, i):
        nums[j] = 1

t2 = time.time()

print("time: ", t2 - t1)
