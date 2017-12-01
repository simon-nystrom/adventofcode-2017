file = open("input-1.txt")
sequence = file.readlines()[0]
file.close()

def solve1(sequence): 
    result = 0
    i = 0
    while i < len(sequence):
        if sequence[i] == sequence[(i + 1) % len(sequence)]:
            result += int(sequence[i])
        i += 1

    return result


def solve2(sequence):
    result = 0
    i = 0
    offset = len(sequence) // 2
    while i < len(sequence):
        if sequence[i] == sequence[(i + offset) % len(sequence)]:
            result += int(sequence[i])
        i += 1

    return result

print(solve1(sequence))
print(solve2(sequence))


