def is_ok(input_str):
    left = 0
    right = len(input_str) - left - 1
    while left <= right:
        if input_str[left] != input_str[right]:
            return False
        left += 1
        right -= 1

    return True


def shortest(input_str):
    print(inp_str)
    # lenght = len(input_str)
    if len(input_str) == 1 or is_ok(input_str):
        print("salammmmmmm")
        return input_str
    else:
        begin = input_str[0]
        end = input_str[-1]

        if begin == end:
            print("fsfa")
            return begin + shortest(input_str[1:-1]) + end
        else:
            print(inp_str[1:])
            same_tail = shortest(input_str[:-1])
            vrkh2 = end + same_tail + end
            cost2 = len(same_tail) - (len(inp_str) - 1) + 2

            sub = inp_str[1:]
            same_head = shortest(sub)

            # return inp_str[1:]
            # same_head = "salam"
            vrkh1 = begin + same_head + begin
            cost1 = len(same_head) - (len(inp_str) - 1) + 2

            if cost1 > cost2:
                return vrkh2
            if cost1 < cost2:
                return vrkh1
            if vrkh1 < vrkh2:
                return vrkh1
            else:
                return vrkh2


inp_str = input()

print(shortest(inp_str))

