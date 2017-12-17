spinlock_step = 328


def solve1(spinlock_step):
    circular_buffer = [0]
    current_position = 0
    for x in range(1, 2018):
        pos = (spinlock_step + current_position) % len(circular_buffer)
        current_position = pos + 1
        circular_buffer.insert(current_position, x)

    return circular_buffer[(current_position + 1) % len(circular_buffer)]


def solve2(spinlock_step):
    current_position_of_zero = 0
    current_position = 0
    after_zero = 0
    current_length = 1
    for x in range(1, 50000001):

        pos = (spinlock_step + current_position) % current_length
        
        if pos == current_position_of_zero:
            after_zero = x
        elif pos < current_position_of_zero:
            current_position_of_zero += 1

        current_position = pos + 1
        current_length += 1

    return after_zero


print(solve1(spinlock_step))
print(solve2(spinlock_step))
