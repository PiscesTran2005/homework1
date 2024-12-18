class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise OverflowError("Stack underflow: attempting to pop from an empty stack")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: attempting to push to a full stack")
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.__queue[0]
