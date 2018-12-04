
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[i]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# noinspection PyShadowingNames
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


n = int(input())

numbers = list()
row_inputs = list()

for i in range(10):
    row_inputs.append(input())

counter = 0
for row_input in row_inputs:
    command = row_input.split(" ")[0]
    if int(command) == 1:
        vote = row_input.split(" ")[1]
        counter += 1
        numbers.append(int(vote))

    else:
        if counter < 3:
            print("No reviews yet")
        else:
            numbers.sort(reverse=True)
            # print(int(counter/3 - 1))
            # print(numbers)
            print(numbers[int(counter/3) - 1])

