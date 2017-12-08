file = open("input-8.txt")
puzzle_input = [x.strip() for x in file.readlines()]
file.close()

print(puzzle_input)


def solve1(puzzle_input):

    registers = {}

    for i in puzzle_input:
        line = i.split()
        print(line)
        reg = line[0]
        instr = line[1]
        amount = int(line[2])
        pred = line[4:len(line)]
        if reg not in registers:
            registers[reg] = 0
        if pred[0] not in registers:
            registers[pred[0]] = 0

        if instr == "dec":
            amount = amount * -1

        if pred[1] == ">":
            if registers[pred[0]] > int(pred[2]):
                registers[reg] += amount
        elif pred[1] == "<":
            if registers[pred[0]] < int(pred[2]):
                registers[reg] += amount
        elif pred[1] == ">=":
            if registers[pred[0]] >= int(pred[2]):
                registers[reg] += amount
        elif pred[1] == "<=":
            if registers[pred[0]] <= int(pred[2]):
                registers[reg] += amount
        elif pred[1] == "==":
            if registers[pred[0]] == int(pred[2]):
                registers[reg] += amount    
        elif pred[1] == "!=":
            if registers[pred[0]] != int(pred[2]):
                registers[reg] += amount
        
        print(line)
        print(registers)

    return max([registers[x] for x in registers])


def solve2(puzzle_input):
    return

print(solve1(puzzle_input))
print(solve2(puzzle_input))
