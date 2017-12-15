from functools import reduce

file1 = open("input-10.txt")
file2 = open("input-10.txt")
puzzle_input_1 = [int(x) for x in file1.read().split(',')]
puzzle_input_2 = [ord(c) for c in file2.read()] + [17, 31, 73, 47, 23]
file1.close()
file2.close()


def sparse_hash(puzzle_input, iterations):
    numbers = [x for x in range(256)]
    current_position = 0
    skip_size = 0
    for i in range(iterations):
        for length in puzzle_input:
            wrapped_reverse(numbers, current_position,
                            current_position + length)
            current_position = (length + skip_size +
                                current_position) % len(numbers)
            skip_size += 1

    return numbers


def wrapped_reverse(array, start, end):

    length = len(array)

    if end > length:

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


def solve1(puzzle_input):
    hashed = sparse_hash(puzzle_input, 1)
    return hashed[0] * hashed[1]


def knot_hash(puzzle_input):
    sparse_hashed = sparse_hash(puzzle_input, 64)

    output = []
    for i in range(0, len(sparse_hashed), 16):
        output.append(reduce((lambda x, y: x ^ y), sparse_hashed[i:i + 16]))

    knot_hash = ""
    for i in output:
        knot_hash += hex(i)[2:].zfill(2)

    return knot_hash



def main():
    print(solve1(puzzle_input_1))
    print(knot_hash(puzzle_input_2))

if __name__ == '__main__':
    main()