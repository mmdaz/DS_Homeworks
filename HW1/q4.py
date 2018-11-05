n, x = map(int, input().split())

weighs = list(input().split())

weighs = [int(x) for x in weighs]

weighs.sort()

weighs_sum = 0
branches = 0

# print(weighs)

end = n - 1
begin = 0
while end != begin and begin != end + 1:

    if weighs[begin] + weighs[end] <= x:
        branches += 1
        begin += 1
        end -= 1

    else:
        branches += 1
        end -= 1

if end == begin:
    branches += 1




print(branches)
