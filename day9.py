file = open("input-9.txt")
puzzle_input = file.read()
file.close()

# print(puzzle_input)

def solve(puzzle_input):
    group_stack = []
    open_garbage = False
    i = -1
    score = 0
    groups = 0
    while i < len(puzzle_input) - 1:
        i += 1
        if puzzle_input[i] == '!':
            i += 1

        elif puzzle_input[i] == '<' and not open_garbage:
            open_garbage = True

        elif puzzle_input[i] == '>':
            open_garbage = False
        
        elif puzzle_input[i] == '{' and not open_garbage:
            group_stack.append('{')

        elif puzzle_input[i] == '}' and not open_garbage:
            groups += 1
            score += len(group_stack)
            group_stack.pop()



    
    return score, groups


print(solve(puzzle_input))