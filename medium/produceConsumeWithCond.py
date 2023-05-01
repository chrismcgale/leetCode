from threading import Condition

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.cond = Condition()
        self.capacity = capacity
        self.que = []

    def enqueue(self, element: int) -> None:
        with self.cond:
            self.cond.wait_for(lambda: len(self.que) < self.capacity)
            self.que.append(element)
            self.cond.notify_all()

    def dequeue(self) -> int:
        with self.cond:
            self.cond.wait_for(lambda: len(self.que) > 0)
            val = self.que.pop(0)
            self.cond.notify_all()
            return val

    def size(self) -> int:
        return len(self.que)