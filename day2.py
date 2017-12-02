file = open("day2-input.txt")
chart = [x.strip() for x in file.readlines()]
file.close()

def solve(chart):
    result = 0;
    for l in chart:
        row = [int(x) for x in l.split('\t')]
        row_max = max(row)
        row_min = min(row)
        result += row_max - row_min
    return result

print(solve(chart))