import re

lines = list(open("input.txt"))
total = 0
for ind, line in enumerate(lines):
    if ind == 0:
        lines_sub = lines[:2]
    elif ind == len(lines) - 1:
        lines_sub = lines[-2:]
    else:
        lines_sub = lines[ind - 1 : ind + 1]
    num_ind = [(m.start(0), m.end(0)) for m in re.finditer(f"\d+", line)]
    for num in num_ind:
        min = num[0] - 1
        max = num[1] + 1
        syms = [re.findall("[^\.|^\d+]", l[min:max]) for l in lines_sub]
        if any(sym for sym in syms):
            total += int(line[num[0] : num[1]])

print(total)
