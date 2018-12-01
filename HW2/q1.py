import heapq


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class Stack:
    def __init__(self, stack_index, nodes):
        self.stack_index = stack_index
        self.nodes = nodes

    def pop(self):
        if self.stack_index > 0 and self.nodes:
            return_value = self.nodes[self.stack_index]
            self.stack_index -= 1
            return return_value

    def push(self, node):
        self.stack_index += 1
        self.nodes.append(node)


class Binary_Search_Tree:
    def __init__(self, keys):
        self.node = None
        self.keys = keys

        for k in keys:
            new_node = Node(k, None, None)
            self.insert_node(new_node)

    def insert_node(self, node):

        pTraverse = self.node
        currentParent = self.node

        while pTraverse:
            currentParent = pTraverse
            if node.data < pTraverse.data:
                pTraverse = pTraverse.left
            else:
                pTraverse = pTraverse.right

        if not currentParent:
            # print("slam")
            self.node = node

        elif node.data < currentParent.data:
            currentParent.left = node
        else:
            currentParent.right = node

    def k_smallest(self, k):
        stack = Stack(0, [0])
        pCrowl = self.node

        while pCrowl:
            stack.push(pCrowl)
            pCrowl = pCrowl.left

        print(stack.nodes)

        while True:
            pCrowl = stack.pop()

            if not pCrowl:
                break

            k -= 1
            if k == 0:
                break

            if pCrowl.right:
                pCrowl = pCrowl.right
                while pCrowl:
                    stack.push(pCrowl)
                    pCrowl = pCrowl.left

        return pCrowl

n = int(input())

numbers = list()
row_inputs = list()

for i in range(10):
    row_inputs.append(input())

for row_input in row_inputs:
    command = row_input.split(" ")[0]
    if int(command) == 1:
        vote = row_input.split(" ")[1]
        numbers.append(int(vote))

    else:
        l = len(numbers)
        if l < 3:
            print("No reviews yet")
        else:
            bst = Binary_Search_Tree(numbers)
            print(bst.k_smallest(l/3))
# print(numbers)
