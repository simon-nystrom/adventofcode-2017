file = open("input-5.txt")
puzzle_input_1 = [int(x.strip()) for x in file.readlines()]
puzzle_input_2 = list(puzzle_input_1)
file.close()


def solve1(puzzle_input):
    current_pos = 0
    steps = 0
    while current_pos < len(puzzle_input):
        steps += 1
        old_pos = current_pos
        current_pos += puzzle_input[current_pos]
        puzzle_input[old_pos] += 1
    return steps


def solve2(puzzle_input):
    current_pos = 0
    steps = 0
    while current_pos < len(puzzle_input):
        steps += 1
        old_pos = current_pos
        current_pos += puzzle_input[current_pos]
        if puzzle_input[old_pos] >= 3:
            puzzle_input[old_pos] -= 1
        else:
            puzzle_input[old_pos] += 1

    return steps


print(solve1(puzzle_input_1))
print(solve2(puzzle_input_2))
