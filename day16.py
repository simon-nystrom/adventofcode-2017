import re

file = open("input-16.txt")
puzzle_input = file.readline().split(',')
file.close()

exchange_pattern = re.compile("x(\d+)\/(\d+)")
spin_pattern = re.compile("s(\d+)")
partner_pattern = re.compile("p(\w)\/(\w)")

programs = [chr(c + ord('a')) for c in range(16)]

def spin(programs, size):
    temp = programs[len(programs) - size:]
    programs[size:] = programs[0:len(programs) - size]
    programs[0:size] = temp


def exchange(programs, a, b):
    temp = programs[a]
    programs[a] = programs[b]
    programs[b] = temp


def partner(programs, a, b):
    a_pos = -1
    b_pos = -1
    for i, p in enumerate(programs):
        if p == a:
            a_pos = i
        if p == b:
            b_pos = i

    exchange(programs, a_pos, b_pos)

def process_instruction(programs, instruction):

    spin_match = spin_pattern.match(instruction)
    if spin_match:
        spin(programs, int(spin_match.group(1)))
        return

    exchange_match = exchange_pattern.match(instruction)
    if exchange_match:
        exchange(programs, int(exchange_match.group(1)),
                    int(exchange_match.group(2)))
        return

    partner_match = partner_pattern.match(instruction)
    if partner_match:
        partner(programs, partner_match.group(1), partner_match.group(2))
        return


def solve1(programs, puzzle_input):
    programs = list(programs)
    for instruction in puzzle_input:
            process_instruction(programs, instruction)
    return "".join(programs)

def solve2(programs, puzzle_input):
    cycle_length = find_cycle_length(programs, puzzle_input)
    for i in range(1000000000 % cycle_length):
        for instruction in puzzle_input:
            process_instruction(programs, instruction)
    return "".join(programs)


def find_cycle_length(programs, puzzle_input):
    programs = list(programs)
    seen = set()
    for i in range(1000000000):
        for j, instruction in enumerate(puzzle_input):
            process_instruction(programs, instruction)
        if "".join(programs) in seen:
            return i
        seen.add("".join(programs))

    return 0


print(solve1(programs, puzzle_input))
print(solve2(programs, puzzle_input))

# bpjahknliomefdgc

map1 = {}
map2 = {}