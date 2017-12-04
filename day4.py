file = open("input-4.txt")
puzzle_input = [x.strip() for x in file.readlines()]
file.close()

def solve1(puzzle_input):
    valid = 0
    for l in puzzle_input:
        valid += 1
        s = set()
        for w in l.split():
            if w in s:
                valid -= 1
                break
            else:
                s.add(w)
    return valid


def solve2(puzzle_input):
    valid = 0
    for l in puzzle_input:
        valid += 1
        s = set()
        for w in l.split():
            _sorted = ''.join(sorted(w))
            if _sorted in s:
                valid -= 1
                break
            else:
                s.add(_sorted)
    return valid



print(solve1(puzzle_input))
print(solve2(puzzle_input))