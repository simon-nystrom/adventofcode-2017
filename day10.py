file = open("input-10.txt")
puzzle_input = [int(x) for x in file.read().split(',')]
file.close()


def solve(puzzle_input):
    numbers = [x for x in range(256)]
    current_position = 0
    skip_size = 0
    for length in puzzle_input:
        wrapped_reverse(numbers, current_position, current_position + length)
        current_position = (length + skip_size + current_position) % len(numbers)
        skip_size += 1

    return numbers[0] * numbers[1]


def wrapped_reverse(array, start, end):
    length = len(array)

    if end >= length:

        start_sublist = array[start:end]
        overflow = end % length
        end_sublist = array[0:overflow]
        sublist = start_sublist + end_sublist
        sublist.reverse()

        array[0:overflow] = sublist[-overflow:]
        array[overflow + length - len(sublist):end] = sublist[:-overflow]

    else:
        sublist = array[start:end]
        sublist.reverse()
        array[start:end] = sublist

    # print(array)


# a = wrapped_reverse([0,1,2,3,4], 4, 8)


# a = wrapped_reverse([4,3,0,1,2], 1, 6)

print(solve(puzzle_input))
