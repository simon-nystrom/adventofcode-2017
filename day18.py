import re
file = open("input-18.txt")
puzzle_input = [x for x in file.read().split('\n')]
file.close()


def jgz(a, b, registers):
    print("jgz", a, b)
    jump_offset = 0
    if a.isalpha():
        if registers[a] <= 0:
            return 0
    elif int(a) <= 0:
        return 0

    if b.isalpha():
        jump_offset = registers[b]
    else:
        jump_offset = int(b)

    return jump_offset


def mul(a, b, registers):
    print("mul", a, b)
    if not a in registers:
        registers[a] = 0
    if b.isalpha():
        registers[a] *= registers[b]
    else:
        registers[a] *= int(b)


def add(a, b, registers):
    print("add", a, b)
    if not a in registers:
        registers[a] = 0
    if b.isalpha():
        registers[a] += registers[b]
    else:
        registers[a] += int(b)


def _set(a, b, registers):
    print("set", a, b)
    if b.isalpha():
        registers[a] = registers[b]
    else:
        registers[a] = int(b)


def mod(a, b, registers):
    print("mod", a, b)
    if not a in registers:
        registers[a] = 0
    if b.isalpha():
        registers[a] %= registers[b]
    else:
        registers[a] %= int(b)


def rcv(a, registers):
    print("rcv", a)
    return registers[a]


def snd(a, registers):
    print("snd", a)
    return registers[a]


pattern = re.compile(
    "((jgz|mul|add|set|mod)\s([a-z0-9]+)\s(-?[a-z0-9]+))|((snd|rcv)\s(\w))")


def solve1(puzzle_input):

    registers = {}
    current_instruction = 0
    last_played_sound = 0

    while True:
        instruction = pattern.match(puzzle_input[current_instruction])

        if instruction.group(2) == "set":
            _set(instruction.group(3), instruction.group(4), registers)

        elif instruction.group(2) == "add":
            add(instruction.group(3), instruction.group(4), registers)

        elif instruction.group(2) == "mod":
            mod(instruction.group(3), instruction.group(4), registers)

        elif instruction.group(2) == "mul":
            mul(instruction.group(3), instruction.group(4), registers)

        elif instruction.group(2) == "jgz":
            jump = jgz(instruction.group(3), instruction.group(4), registers)
            if jump != 0:
                current_instruction += jump
                continue

        elif instruction.group(6) == "snd":
            last_played_sound = snd(instruction.group(7), registers)

        elif instruction.group(6) == "rcv":
            if rcv(instruction.group(7), registers) > 0:
                return last_played_sound

        current_instruction += 1

print(solve1(puzzle_input))