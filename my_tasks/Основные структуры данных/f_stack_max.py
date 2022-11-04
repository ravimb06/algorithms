class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return 'error'
        self.items.pop()
    
    def get_max(self):
        if not self.items:
            return 'None'
        max_item = self.items[0]
        for i in self.items:
            if i > max_item:
                max_item = i
        return max_item


max_stack = StackMax()
cnt_commands = int(input())
result = []
for i in range(cnt_commands):
    command = input().split()
    if command[0] == 'push':
        max_stack.push(int(command[1]))
    if command[0] == 'pop':
        pop_result = max_stack.pop()
        if pop_result:
            result.append(pop_result)
    if command[0] == 'get_max':
        result.append(max_stack.get_max())
for i in result:
    print(i)
