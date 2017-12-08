file = open("input-8.txt")
puzzle_input = [x.strip() for x in file.readlines()]
file.close()

def solve(puzzle_input):

    registers = {}
    highest_ever = 0

    for i in puzzle_input:
        line = i.split()
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
        
        highest_ever = max(highest_ever, max([registers[x] for x in registers]))

    
    return (max([registers[x] for x in registers]), highest_ever)


print(solve(puzzle_input))
