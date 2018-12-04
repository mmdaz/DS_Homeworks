import heapq

# left_count = 0


class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.left_count = 0

    def insert_tree(self, x):
        # print("l : {}".format(self.left_count))

        if self.data:
            if x <= self.data:
                if self.left is None:
                    # global left_count
                    self.left_count += 1
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

        # print(self.left_count)
        if self.left_count + 1 == k:
            print("salam")
            print(self.data)
            return self.data
        if k > self.left_count:
            k = k - (self.left_count + 1)
            self.right.k_th_smallest_data(k)
        else:
            self.left.k_th_smallest_data(k)

        # pTraverse = self.data
        # # global left_count
        # print(str(k) + "k")
        # # print(str(left_count) + "dfg")
        # while pTraverse:
        #     print(str(self.data) + "sdf")
        #     if pTraverse.left_count + 1 == k:
        #         print("salam")
        #         return self.data
        #     elif k > pTraverse.left_count:
        #         k = k - (pTraverse.left_count + 1)
        #         pTraverse = pTraverse.right
        #     else:
        #         pTraverse = pTraverse.left

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
        bst.insert_tree(int(vote))

    else:
        if counter < 3:
            print("No reviews yet")
        else:
            print("sdfg{}".format(bst.k_th_smallest_data(int(counter / 3))))

bst.print_tree()
print(counter)
# print(bst.left_count)
