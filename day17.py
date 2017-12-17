spinlock_step = 328

circular_buffer = [0]

current_size = 1
current_position = 0
for x in range(1, 50000000):
    pos = (spinlock_step + current_position) % len(circular_buffer)
    # print(pos)
    current_position = pos +  1
    circular_buffer.insert(current_position, x)

print(circular_buffer[(current_position + 1) % len(circular_buffer)])
