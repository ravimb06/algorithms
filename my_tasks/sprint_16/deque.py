# 73828382

class Deque:
    def __init__(self, m):
        self.__queue = [None] * m
        self.__max_size = m
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0
        
    def push_back(self, x):
        if self.__size == self.__max_size:
            raise OverflowError('Недостаточно памяти.')
        self.__queue[self.__tail] = x
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def push_front(self, x):
        if self.__size == self.__max_size:
            raise OverflowError('Недостаточно памяти.')
        self.__queue[self.__head - 1] = x
        self.__head = (self.__head - 1) % self.__max_size
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('Нет доступных объектов.')
        else:
            element = self.__queue[self.__head]
            self.__queue[self.__head] = None
            self.__head = (self.__head + 1) % self.__max_size
            self.__size -= 1
            return element

    def pop_back(self):
        if self.is_empty():
            raise IndexError('Нет доступных объектов.')
        else:
            element = self.__queue[self.__tail-1]
            self.__queue[self.__tail-1] = None
            self.__tail = (self.__tail - 1) % self.__max_size
            self.__size -= 1
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
