import re
file = open("input-18.txt")
puzzle_input = [x for x in file.read().split('\n')]
file.close()


def jgz(a, b, registers):
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
    if not a in registers:
        registers[a] = 0
    if b.isalpha():
        registers[a] *= registers[b]
    else:
        registers[a] *= int(b)


def add(a, b, registers):
    if not a in registers:
        registers[a] = 0
    if b.isalpha():
        registers[a] += registers[b]
    else:
        registers[a] += int(b)


def _set(a, b, registers):
    if b.isalpha():
        registers[a] = registers[b]
    else:
        registers[a] = int(b)


def mod(a, b, registers):
    if not a in registers:
        registers[a] = 0
    if b.isalpha():
        registers[a] %= registers[b]
    else:
        registers[a] %= int(b)


def rcv(a, registers):
    return registers[a]


def snd(a, registers):
    return registers[a]


pattern = re.compile(
    "((jgz|mul|add|set|mod)\s([a-z0-9]+)\s(-?[a-z0-9]+))|((snd|rcv)\s(\w))")


def process_two_piece_instruction(instruction, a, b, register):
    if instruction == "set":
        _set(a, b, register)

    elif instruction == "add":
        add(a, b, register)

    elif instruction == "mod":
        mod(a, b, register)

    elif instruction == "mul":
        mul(a, b, register)


def solve1(puzzle_input):

    register = {}
    current_instruction = 0
    last_played_sound = 0

    while True:
        instruction = pattern.match(puzzle_input[current_instruction])

        process_two_piece_instruction(
            instruction.group(2),
            instruction.group(3),
            instruction.group(4),
            register
        )

        if instruction.group(2) == "jgz":
            jump = jgz(instruction.group(3), instruction.group(4), register)
            if jump != 0:
                current_instruction += jump
                continue

        elif instruction.group(6) == "snd":
            last_played_sound = snd(instruction.group(7), register)

        elif instruction.group(6) == "rcv":
            if rcv(instruction.group(7), register) > 0:
                return last_played_sound

        current_instruction += 1


def _rcv(a, register, message_queue):
    if len(message_queue) == 0:
        return False
    register[a] = message_queue[0]
    del message_queue[0]
    return True


def _snd(a, register, message_queue):
    message_queue.append(register[a])


def solve2(puzzle_input):
    register_one = {"p": 1}
    message_queues = [[], []]
    registers = [{"p": 0}, {"p": 1}]
    pcs = [0, 0]
    active_program = 0
    sends = [0, 0]
    while True:
        instruction = pattern.match(puzzle_input[pcs[active_program]])

        process_two_piece_instruction(
            instruction.group(2),
            instruction.group(3),
            instruction.group(4),
            registers[active_program]
        )

        if instruction.group(2) == "jgz":
            jump = jgz(instruction.group(3), instruction.group(
                4), registers[active_program])
            if jump != 0:
                pcs[active_program] += jump
                continue

        elif instruction.group(6) == "snd":
            _snd(instruction.group(7),
                 registers[active_program], message_queues[active_program])
            sends[active_program] += 1

        elif instruction.group(6) == "rcv":
            if len(message_queues[0]) == 0 and len(message_queues[1]) == 0:
                return sends[1]
            if not _rcv(instruction.group(7), registers[active_program], message_queues[active_program ^ 1], sends):
                active_program ^= 1
                continue

        pcs[active_program] += 1


print(solve1(puzzle_input))
print(solve2(puzzle_input))
