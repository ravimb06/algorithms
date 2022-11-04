# 73829112

import operator


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            raise IndexError

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


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
