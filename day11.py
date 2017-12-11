file = open("input-11.txt")
puzzle_input = [x for x in file.read().split(',')]
file.close()


def solve(puzzle_input):
    x = y = 0
    furthest = 0
    for d in puzzle_input:

        if d == "ne":
            x += 1
        elif d == "sw":
            x -= 1
        elif d == "nw":
            y += 1
            x += 1
        elif d == "se":
            y -= 1
            x -= 1
        elif d == "n":
            y += 1
        elif d == "s":
            y -= 1

        furthest = max(furthest, max(abs(x), abs(y)))

    return max(abs(x), abs(y)), furthest


print(solve(puzzle_input))
