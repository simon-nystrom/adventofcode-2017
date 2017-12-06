file = open("input-6.txt")
puzzle_input = list(map(int, [x.strip().split('\t') for x in file.readlines()][0]))
file.close()

def solve(puzzle_input):

    puzzle_input_string = ""
    seen = {}
    cycles = 0

    while True:
        
        cycles += 1
        m = -1
        maxIndex = 0
        for i, x in enumerate(puzzle_input):
            if x > m:
                m = x
                maxIndex = i
        puzzle_input[maxIndex] = 0
        i = 0
        while i < m:
            puzzle_input[(maxIndex + 1 + i) % len(puzzle_input)] += 1
            i += 1
        puzzle_input_string = "".join((list(map(str, puzzle_input))))
        if puzzle_input_string in seen:
            break
        seen[puzzle_input_string] = cycles

    return (cycles, cycles - seen[puzzle_input_string])

print(solve(puzzle_input)) # Prints both solutions as a tuple