# left_count = 0


class Node:
    def __init__(self, data):
        self.left_count = 0
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insert_in_tree(self, x):
        pTraverse = self.root
        current_node = self.root

        if self.root is None:
            self.root = x
        else:
            while pTraverse:
                current_node = pTraverse
                if x.data < pTraverse.data:
                    pTraverse.left_count += 1
                    pTraverse = pTraverse.left
                else:
                    pTraverse = pTraverse.right
            if x.data < current_node.data:
                current_node.left = x
            else:
                current_node.right = x

    def kth_smallest_number(self, k):
        result = -1
        pTraverce = self.root
        while pTraverce:
            if pTraverce.left_count + 1 == k:
                result = pTraverce.data
                break
            elif pTraverce.left_count < k:
                k = k - (pTraverce.left_count + 1)
                pTraverce = pTraverce.right
            else:
                pTraverce = pTraverce.left

        return result


def insert(root, node):
    if root[0] is None:
        print("a im hrerrrrrrr")
        root[0] = node
    else:
        if root[0].data < node.data:
            if root[0].right is None:

                root[0].right = node
            else:
                root[0].left_count += 1
                insert(root, node)
        else:
            if root[0].left is None:
                root[0].left = node
            else:
                insert(root, node)


def kthSmallest(arr, k):
    # Sort the given array
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[k - 1]


def k_th_smallest(root, k):
    pTraverse = root
    while pTraverse:
        print(pTraverse.left_count)
        if pTraverse.left_count + 1 == k:
            print("salam")
            return pTraverse.data
        elif k > pTraverse.left_count:
            k = k - (pTraverse.left_count + 1)
            pTraverse = pTraverse.right
        else:
            pTraverse = pTraverse.left


n = int(input())
numbers = list()
row_inputs = list()

# for i in range(10):
#     row_inputs.append(input())
root = [None]
counter = 0
bst = BinarySearchTree(None)
inps = []
for i in range(n):
    # raw_input = input()
    inps.append(input())
    if len(inps[i]) == 1:
        if counter < 3:
            print("No reviews yet")
        else:
            print(bst.kth_smallest_number((counter - int(counter / 3) + 1)))

    else:
        vote = int(inps[i].split(" ")[1])
        bst.insert_in_tree(Node(vote))
        counter += 1

#
# for row_input in row_inputs:
#     command = row_input.split(" ")[0]
#     if int(command) == 1:
#         vote = row_input.split(" ")[1]
#         counter += 1
#         numbers.append(int(vote))
#         bst.insert_in_tree(Node(data=int(vote)))
#         # insert(root, Node(int(vote)))
#
#     else:
#         if counter < 3:
#             print("No reviews yet")
#         else:
#             print(bst.kth_smallest_number((counter -  int(counter /3) +1)))

