class Stack:

    def __init__(self):
        self.stack = list()
        self.indexes = list()

    def push(self, parentheses):
        if parentheses == "(":
            self.stack.append(parentheses)
        else:
            i_mi = []


phrase = input()

counter = 0
m_indexes = list()
indexes = list()
stack = list()
for c in phrase[1:]:


print(m_indexes)
