# 2020-06-02
# Создать класс MyArray и реализовать в нем методы min, max, avg, sum.
# - Понятие, что такое класс и объект (экземпляр класса)
# - Понятие, что такое кеш
# - Замер скорости выполнения блока кода
import time
import numpy as np


class MyArray:

    def __init__(self, my_array):
        self.array = my_array
        self.cache_min = None
        self.cache_max = None
        self.cache_sum = None

    def __calc(self):
        mini = None
        maxi = None
        sum = 0
        for i in self.array:
            sum += i
            if None == mini or mini > i:
                mini = i
            if None == maxi or maxi < i:
                maxi = i
        self.cache_min = mini
        self.cache_max = maxi
        self.cache_sum = sum

    def min(self):
        if self.cache_min is None:
            self.__calc()
        return self.cache_min

    def max(self):
        if self.cache_max is None:
            self.__calc()
        return self.cache_max

    def sum(self):
        if self.cache_sum is None:
            self.__calc()
        return self.cache_sum

    def avg(self):
        if self.cache_sum is None:
            self.__calc()
        avg = self.cache_sum / len(self.array)
        return avg

####################################################################


length = 10000000

data = np.random.random(length)

print(len(data))

t1 = time.time()
myarr = MyArray(data)

print("min: ", myarr.min())
print("max: ", myarr.max())
print("sum: ", myarr.sum())
print("avg: ", myarr.avg())
t2 = time.time()
print(t2-t1)
