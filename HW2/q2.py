import heapq

n = int(input())

numbers = input()

numbers = [int(n) for n in numbers.split(" ")]

heapq.heapify(numbers)
result = 0

for i in range(n - 1):
    temp = heapq.heappop(numbers)
    temp += heapq.heappop(numbers)
    result += temp
    heapq.heappush(numbers, temp)
    # print(numbers)
    # heapq.heapify(numbers)

print(result + numbers[0])
