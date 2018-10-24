n = int(input())

commands = list()
stack = list()

for i in range(0, n):
    command = input()
    if command.split(" ")[0] == "push":
        stack.append(int(command.split(" ")[1]))
    elif command.split(" ")[0] == "pop":
        stack.pop()
    else:
        print(min(stack))
