from collections import deque
from queue import Queue

x = int(input())

commands = list()
queue = deque()
undo_list = list()
for i in range(0, x):
    commands.append(input())

for command in commands:
    if command.split(" ")[0] == "enqueue":
        x = int(command.split(" ")[1])
        queue.appendleft(x)
        undo_list.append("pop".format(x))

    elif command.split(" ")[0] == "pop":
        pop_element = queue.pop()
        print(pop_element)
        undo_list.append("enqueue {}".format(pop_element))

    else:
        if undo_list[-1].__contains__("enqueue"):
            # print(undo_list[-1])
            # print("qs{}".format(queue.qsize()))
            queue.append(int(undo_list[-1].split(" ")[1]))
            undo_list.pop()
        else:
            queue.popleft()
            undo_list.pop()
