from functools import reduce
from day10 import knot_hash

puzzle_input = [list(map(ord, string))
                for string in ["stpzcrnm-" + str(i) for i in range(128)]]
for l in puzzle_input:
    l.extend([17, 31, 73, 47, 23])


def to_binary(hex_num):
    parts = []
    for n in hex_num:
        parts.append(bin(int(n, 16))[2:].zfill(4))
    return "".join(parts)


def solve1(puzzle_input):
    total = 0
    for l in puzzle_input:
        binary_string = to_binary(knot_hash(l))
        total += len(binary_string.replace("0", ""))
    return total


def solve2(puzzle_input):
    grid = [[0 for x in range(128)] for y in range(128)]
    region = 1
    for i, l in enumerate(puzzle_input):
        binary_string = to_binary(knot_hash(l))
        for j, c in enumerate(binary_string):
            if c == "1":
                grid[i][j] = "#"
            else:
                grid[i][j] = "."
    for y in range(len(grid)):
        # print("x: ", x)
        for x in range(len(grid[y])):
            if not flood_fill(grid, x, y, str(region)):
                continue
            region += 1

    return region - 1


def flood_fill(grid, x, y, region):
    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid):
        return False
    if grid[x][y] != "#":
        return False
    grid[x][y] = region
    flood_fill(grid, x + 1, y, region)
    flood_fill(grid, x - 1, y, region)
    flood_fill(grid, x, y + 1, region)
    flood_fill(grid, x, y - 1, region)

    return True


print(solve1(puzzle_input))
print(solve2(puzzle_input))
