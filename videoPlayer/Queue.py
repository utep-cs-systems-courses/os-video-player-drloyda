from threading import Semaphore, Lock
class Queue:
    def __init__(self, value=10):
        self.queue = []
        self.used_cells = Semaphore(value=value)
        self.empty_cells = Semaphore(value=0)
        self.lock = Lock()

    def put(self, item):
        self.used_cells.acquire()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.empty_cells.release()

    def get(self):
        while not self.size():
            self.empty_cells.acquire()
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        self.used_cells.release()
        return item

    def size(self):
        return len(self.queue)

    def empty(self):
        return not self.size()

