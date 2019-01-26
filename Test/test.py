def test(inp):
    if len(inp) == 1:
        return 1
    print(inp)
    test(inp[1:])

test("safaf")