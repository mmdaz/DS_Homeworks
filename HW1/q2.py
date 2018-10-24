x = int(input())

commands = list()
queue = list()
poped_list = list()
for i in range(0, x):
    commands.append(input())

for command in commands:
    if command.split(" ")[0] == "enqueue":
        queue.insert(0, int(command.split(" ")[1]))
    elif command.split(" ")[0] == "pop":
       poped_list.append(queue.pop())

print(poped_list)
