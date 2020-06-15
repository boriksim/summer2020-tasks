class BaseList:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0


class BaseListException(Exception):
    pass


class StackException(BaseListException):
    pass


class StackEmptyException(StackException):
    pass


class QueueException(BaseListException):
    pass


class QueueEmptyException(StackException):
    pass


class Stack(BaseList):

    def push(self, value):
        # добавить элемент в стек
        self.list.append(value)

    def pop(self):
        # получить элемент и удалить его
        if self.is_empty():
            raise StackEmptyException()
        else:
            last = self.list[-1]
            self.list = self.list[:-1]
            return last

    def top(self):
        # получить элемент
        if self.is_empty():
            raise StackEmptyException()
        else:
            return self.list[-1]


class Queue(BaseList):

    def append(self, value):
        # добавить элемент в очередь
        self.list.append(value)

    def fetch(self):
        # получить элемент и удалить его
        if self.is_empty():
            raise QueueEmptyException()
        else:
            first = self.list[0]
            self.list = self.list[1:]
            return first

    def head(self):
        # получить элемент
        if self.is_empty():
            raise QueueEmptyException()
        else:
            return self.list[0]


def quick_sort(list):
    if len(list) == 0:
        return list
    pivot = list[0]
    p_count = 0
    lA = []
    rA = []
    for x in list:
        if x < pivot:
            lA.append(x)
        elif x > pivot:
            rA.append(x)
        else:
            p_count += 1
    return quick_sort(lA) + [pivot] * p_count + quick_sort(rA)


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
