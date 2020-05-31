# 2020-05-31
# Сортировка массива методом bubble sort
import random

length = 100
nums = []


def sort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


for x in range(length):
    nums.append(random.randint(0, 100))

sort(nums)

for y in nums:
   print(y)
