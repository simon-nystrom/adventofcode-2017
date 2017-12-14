file = open("input-13.txt")
puzzle_input = [list(map(int, x.strip().replace(":", "").split(' '))) for x in file.readlines()]
file.close()

def solve(puzzle_input):

    severity = 0
    scanner_pos = 0
    for i, depth in puzzle_input:
        loop = i // (depth - 1)
        scanner_pos = i % (depth - 1)
        if loop > 0 and loop % 2 != 0:
            scanner_pos = depth - 1 - scanner_pos
        if scanner_pos == 0:
            severity += i * depth

    return severity

def solve1(puzzle_input):
    scanner_pos = 0
    delay = 0
    max_reach = 0
    detected = True
    while (detected):
        for i, depth in puzzle_input:
            detected = False
            loop = (i + delay) // (depth - 1)
            scanner_pos = (i + delay) % (depth - 1)
            if loop > 0 and loop % 2 != 0:
                scanner_pos = depth - 1 - scanner_pos
            if scanner_pos == 0:
                detected = True
                break
        delay += 1

    # print(max_reach)
    return delay - 1


print(solve(puzzle_input))
print(solve1(puzzle_input))

