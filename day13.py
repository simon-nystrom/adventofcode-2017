file = open("input-13.txt")
puzzle_input = [x.strip().replace(":", "").split(' ') for x in file.readlines()]
file.close()

def solve(puzzle_input):

    current_position = 0
    scanners = {}
    scanner_pos = 0
    for i, scanner in enumerate(puzzle_input):
        scanners[scanner[0]] = int(scanner[1]) - 1
        loop = i // scanners["0"]
        scanner_pos = i % scanners["0"]
        if loop > 0 and loop % 2 != 0:
            scanner_pos = scanners["0"] - scanner_pos

            
        print(scanner_pos)
        


    return "end"


print(solve(puzzle_input))

