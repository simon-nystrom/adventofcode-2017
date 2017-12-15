
a_start = 289
b_start = 629
a_factor = 16807
b_factor = 48271


def generator_1(previous, factor, divisor):
    while True:
        previous = (previous * factor) % divisor
        yield previous


def generator_2(previous, factor, divisor, multiples_of):
    while True:
        previous = (previous * factor) % divisor
        while previous % multiples_of != 0:
            previous = (previous * factor) % divisor
        yield previous


def solve1(a_start, b_start, a_factor, b_factor):
    a = generator_1(a_start, a_factor, 2147483647)
    b = generator_1(b_start, b_factor, 2147483647)
    result = 0
    mask = 0xffff
    for i in range(40000000):
        if (next(a) & mask) ^ (next(b) & mask) == 0:
            result += 1
    return result


def solve2(a_start, b_start, a_factor, b_factor):
    a = generator_2(a_start, a_factor, 2147483647, 4)
    b = generator_2(b_start, b_factor, 2147483647, 8)
    result = 0
    mask = 0xffff
    for i in range(5000000):
        if (next(a) & mask) ^ (next(b) & mask) == 0:
            result += 1
    return result


print(solve1(a_start, b_start, a_factor, b_factor))
print(solve2(a_start, b_start, a_factor, b_factor))
