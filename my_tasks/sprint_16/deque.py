# 73828382

class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_size = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
        
    def push_back(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, x):
        if self.size != self.max_size:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            raise OverflowError

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        else:
            element = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return element

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        else:
            element = self.queue[self.tail-1]
            self.queue[self.tail-1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return element


if __name__ == '__main__':
    commands = int(input())
    dq_size = int(input())
    dq = Deque(dq_size)

    for _ in range(commands):
        cmd = input().split()
        if len(cmd) == 2:
            try:
                method = getattr(dq, cmd[0])
                method(cmd[1])
            except OverflowError:
                print('error')

        elif len(cmd) == 1:
            try:
                method = getattr(dq, cmd[0])
                print(method())
            except IndexError:
                print('error')
