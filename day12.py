import re

file = open("input-12.txt")
puzzle_input = [(re.sub(",|<->\s", "", x.strip())).split(" ")[1:]
                for x in file.readlines()]
file.close()


def solve(puzzle_input):
    return len(find_all_connections_to(0, set("0"), puzzle_input)), all_groups(puzzle_input)


def find_all_connections_to(index, connected, puzzle_input):
    to_visit = puzzle_input[index]
    for x in to_visit:
        if x not in connected:
            connected.add(x)
            find_all_connections_to(int(x), connected, puzzle_input)
    return connected


def all_groups(puzzle_input):
    groups = 0
    connections = set()
    for i in range(len(puzzle_input)):
        if puzzle_input[i][0] in connections:
            continue
        for connection in find_all_connections_to(i, set(str(i)), puzzle_input):
            connections.add(connection)
        groups += 1
    return groups


print(solve(puzzle_input))
