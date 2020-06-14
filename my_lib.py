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