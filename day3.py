
# My spiral for part 1 was designed to start at 0, so we have to subtract 1 for my input.
puzzle_input_1 = 312051 - 1
puzzle_input_2 = 312051


def solve1(puzzle_input):
    current_sum = layer = 0
    corners = previous_corners = [0, 0, 0, 0]
    corner = offset = 2
    while current_sum < puzzle_input - layer * 8:
        previous_corners = corners
        corners = [corner + offset * x for x in range(4)]
        offset += 2
        corner = corners[-1] + offset
        current_sum += layer * 8
        layer += 1

    previous_corners.extend(corners)
    for i in range(len(previous_corners) - 1):
        if puzzle_input >= previous_corners[i] and puzzle_input <= previous_corners[i + 1]:
            center = (previous_corners[i] + previous_corners[i + 1]) // 2
            return layer + abs(puzzle_input - center)


def needed_layers(puzzle_input):
    current_sum = layer = 0
    while current_sum < puzzle_input - layer * 8:
        current_sum += layer * 8
        layer += 1
    return layer


def sum_adjacent(grid, row, col):

    result = 0

    result += grid[row + 1][col]
    result += grid[row + 1][col + 1]
    result += grid[row + 1][col - 1]

    result += grid[row - 1][col]
    result += grid[row - 1][col + 1]
    result += grid[row - 1][col - 1]

    result += grid[row][col - 1]
    result += grid[row][col + 1]

    return result


def spiral_loop(grid, row, col, offset):
    while(True):
        col += 1
        current = sum_adjacent(grid, row, col)
        grid[row][col] = current
        yield current
        for _ in range(offset - 1):
            row -= 1
            current = sum_adjacent(grid, row, col)
            grid[row][col] = current
            yield current
        for _ in range(offset):
            col -= 1
            current = sum_adjacent(grid, row, col)
            grid[row][col] = current
            yield current
        for _ in range(offset):
            row += 1
            current = sum_adjacent(grid, row, col)
            grid[row][col] = current
            yield current
        for _ in range(offset):
            col += 1
            current = sum_adjacent(grid, row, col)
            grid[row][col] = current
            yield current
        offset += 2


def solve2(puzzle_input):
    current_value = 0
    layers = needed_layers(puzzle_input) + 5
    grid = [[0 for x in range(layers)] for y in range(layers)]
    row = col = layers // 2  # Start in the middle
    grid[row][col] = 1
    spiral_gen = spiral_loop(grid, row, col, 2)
    while current_value <= puzzle_input:
        current_value = next(spiral_gen)
    return current_value


print(solve1(puzzle_input_1))
print(solve2(puzzle_input_2))
