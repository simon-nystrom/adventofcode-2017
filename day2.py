file = open("input-2.txt")
chart = [x.strip() for x in file.readlines()]
file.close()

def row_result_max_min(row):
    return max(row) - min (row)

def row_result_div(row):
    for i, x in enumerate(row):
        for j, y in enumerate(row):
            if x % y == 0 and i != j:
                return x // y
            elif y % x == 0 and i != j:
                return  y // x

def solve(chart, row_op):
    result = 0
    for l in chart:
        row = [int(x) for x in l.split('\t')]
        result += row_op(row)
    return result

print(solve(chart, row_result_max_min))
print(solve(chart, row_result_div))
