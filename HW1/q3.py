class Stack:

    def __init__(self):
        self.stack = list()
        self.indexes = list()
        self.result = 0

    def push(self, parentheses):
        self.stack.append(parentheses)

    def pop(self):
        self.stack.pop()
        self.result += 1
        if len(self.stack) == 0:
            # self.result = self.result * 2 -1
            self.indexes.append(self.result)
            self.result = 0


stack = Stack()
n = int(input())
phrase = input()

for c in phrase:
    if c == "(":
        stack.push(c)
        # print(stack.stack)
    else:
        stack.pop()

print(2 * max(stack.indexes) - 1)
