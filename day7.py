file = open("input-7.txt")
puzzle_input = [x.strip() for x in file.readlines()]
file.close()


def solve1(puzzle_input):
    # s = ()
    defined = {}
    last_insert = ""
    while len(defined) < len(puzzle_input):
        for i in puzzle_input:
            split = i.split(" ")
            if split[0] in defined:
                continue
            if (len(split) == 2):
                defined[split[0]] = split[1][1:-1]
                last_insert = split[0]
            else: 
                areDefined = 0
                length = len(split[3:])
                for j in split[3:]:
                    j = j.replace(",", "")
                    if j in defined:
                        areDefined += 1
                        if areDefined == length:
                            defined[split[0]] = split[1][1:-1]
                            last_insert = split[0]
        #         else:
        #             stack.append(split[0])
        # print (stack)
                    
    
    return last_insert


def solve2(puzzle_input):
    return

print(solve1(puzzle_input))
print(solve2(puzzle_input))
