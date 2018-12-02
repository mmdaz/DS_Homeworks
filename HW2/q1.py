import heapq

left_count = 0


class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        # self.left_count = left_count

    def insert_tree(self, x):
        # print("l : {}".format(self.left_count))
        if self.data:
            if x <= self.data:
                if self.left is None:
                    global left_count
                    left_count += 1
                    self.left = Binary_Search_Tree(data=x)
                else:
                    self.left.insert_tree(x=x)
            elif x > self.data:
                if self.right is None:
                    self.right = Binary_Search_Tree(data=x)
                else:
                    self.right.insert_tree(x=x)
        else:
            self.data = x

    def k_th_smallest_data(self, k):

        pTraverse = self.data
        global left_count
        print(str(k) + "k")
        # print(str(left_count) + "dfg")
        while self.data:
            print(self.data + "sdf")
            if left_count + 1 == k:
                print("salam")
                return self.data
            elif k > left_count:
                k = k - (left_count + 1)
                self.data = self.right
            else:
                self.data = self.left

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


n = int(input())

numbers = list()
row_inputs = list()

for i in range(10):
    row_inputs.append(input())

bst = Binary_Search_Tree(data=None)
counter = 0
for row_input in row_inputs:
    command = row_input.split(" ")[0]
    if int(command) == 1:
        vote = row_input.split(" ")[1]
        counter += 1
        bst.insert_tree(vote)

    else:
        if counter < 3:
            print("No reviews yet")
        else:
            print(bst.k_th_smallest_data(int(counter / 3)))

# bst.print_tree()
# print(bst.left_count)
