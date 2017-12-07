file = open("input-7.txt")
puzzle_input = [x.strip() for x in file.readlines()]
file.close()


def find_bottom_and_build_maps(puzzle_input):
    stack = []
    values = {}
    connections = {}
    last = None
    while len(values) < len(puzzle_input):
        for i in puzzle_input:
            split = i.split(" ")
            if split[0] in values:
                continue
            if len(split) == 2:
                values[split[0]] = int(split[1][1:-1])
            else:
                are_defined = 0
                targets = [x.replace(",", "") for x in split[3:]]
                connections[split[0]] = targets
                for j in targets:
                    if j in values:
                        are_defined += 1
                        if are_defined == len(targets):
                            values[split[0]] = int(split[1][1:-1])
                last = split[0]

    return (values, last, connections)


def find_bad_stack(root, values, connections, diff):

    stack_weights = []
    if root in connections:
        for con in connections[root]:
            stack_weights.append(stack_weight(con, values, connections))

        if len(set(x[1] for x in stack_weights)) == 1:
            return (root, diff)

        bad_index = -1
        first = stack_weights[0][1]
        for i in range(len(stack_weights[1:-1])):
            current = stack_weights[i][1]
            _next = stack_weights[i + 1][1]
            if first != current and current == _next:
                bad_index = 0
            elif first == current and current != _next:
                bad_index = i + 1

        bad_node = stack_weights[bad_index][0]
        bad_node_weight = stack_weights[bad_index][1]

        good_index = (bad_index + 1) % len(stack_weights)
        good_stack_weight = stack_weights[good_index][1]

        return find_bad_stack(bad_node, values, connections, good_stack_weight - bad_node_weight)


def stack_weight(root, values, connections):

    total_weight = 0
    if root in connections:
        for con in connections[root]:
            total_weight += stack_weight(con, values, connections)[1]

    return (root, total_weight + values[root])


def solve1(puzzle_input):

    _, bottom, _ = find_bottom_and_build_maps(puzzle_input)

    return bottom


def solve2(puzzle_input):

    values, bottom, connections = find_bottom_and_build_maps(puzzle_input)

    bad_stack_and_diff = find_bad_stack(bottom, values, connections, 0)

    return values[bad_stack_and_diff[0]] + bad_stack_and_diff[1]


print(solve1(puzzle_input))
print(solve2(puzzle_input))
