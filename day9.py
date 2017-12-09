file = open("input-9.txt")
puzzle_input = file.read()
file.close()


def solve(puzzle_input):
    group_stack = []
    open_garbage = False
    score = removed_garbage = i = 0
    while i < len(puzzle_input):

        if puzzle_input[i] == '!':
            i += 1

        elif puzzle_input[i] == '<' and not open_garbage:
            open_garbage = True

        elif puzzle_input[i] == '>':
            open_garbage = False

        elif puzzle_input[i] == '{' and not open_garbage:
            group_stack.append('{')

        elif puzzle_input[i] == '}' and not open_garbage:
            score += len(group_stack)
            group_stack.pop()

        elif open_garbage:
            removed_garbage += 1

        i += 1

    return score, removed_garbage


print(solve(puzzle_input))
