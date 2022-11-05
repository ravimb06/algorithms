# 73902771

import operator


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        if len(self.__items) > 0:
            return self.__items.pop()
        raise IndexError('Нет доступных объектов.')

    def size(self):
        return len(self.__items)


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


a = Stack()
OPERATORS = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'floordiv'
}

if __name__ == '__main__':
    for i in input().split():
        if isint(i) == True:
            a.push(int(i))
        else:
            if a.size() != 0:
                second_int = a.pop()
                first_int = a.pop()
                attr = getattr(operator, OPERATORS[i])
                method = lambda x, y: attr(x, y)
                result = method(first_int, second_int)
                a.push(result)

    print(a.pop())
