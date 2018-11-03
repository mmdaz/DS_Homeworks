n, x = map(int, input().split())

weighs = list(input().split())

weighs = [int(x) for x in weighs]

weighs.sort()

weighs_sum = 0
branches = 0

print(weighs)

for w in weighs:
    weighs_sum += w
    if weighs_sum >= 10:
        if weighs_sum == x:
            branches += 1


print(branches)