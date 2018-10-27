n = int(input())

commands = []
stack = []
min = int()

# for i in range(n):
#     commands.append(input())

for i in range(n):
    command = input()
    if command.__contains__("push"):
        x = int(command.split()[1])
        if len(stack) == 0:
            min = x
            stack.append(x)
        elif x < min:
            stack.append(2*x - min)
            min = x
        else:
            stack.append(x)
    elif command.__contains__("pop"):
        top = stack.pop()
        if top < min:
            min = 2 * min - top
    else:
        print(min)
