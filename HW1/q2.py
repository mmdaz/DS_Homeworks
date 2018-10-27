from collections import deque
from queue import Queue


x = int(input())

commands = list()
queue = Queue()
undo_list = list()
for i in range(0, x):
    commands.append(input())

for command in commands:
    if command.split(" ")[0] == "enqueue":
        x = int(command.split(" ")[1])
        queue.put_nowait(x)
        undo_list.append("pop".format(x))

    elif command.split(" ")[0] == "pop":
        # print(queue[0])
        pop_element = queue.get()
        print(pop_element)
        undo_list.append("enqueue {}".format(pop_element))



    else:
        if undo_list[-1].__contains__("enqueue"):
            # print(undo_list[-1])
            queue.put(int(undo_list[-1].split(" ")[1]))
            # print("q0" + str(queue[0]))
            undo_list.remove(undo_list[-1])
            continue
        else:
            # print(undo_list[-1])
            queue.get()
            undo_list.remove(undo_list[-1])
