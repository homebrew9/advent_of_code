import sys
import re
from collections import defaultdict

def isAdjacent(r, c):
    directions = [ [-1,-1], [-1,0], [-1,1],
                   [0,-1], [0,1],
                   [1,-1], [1,0], [1,1]
                 ]
    for dr, dc in directions:
        rnew, cnew = r + dr, c + dc
        if 0 <= rnew < rows and 0 <= cnew < cols:
            if lines[rnew][cnew] == '*':
                gears.add((rnew, cnew))
            if not lines[rnew][cnew].isdigit() and lines[rnew][cnew] != '.':
                return True
    return False

# Main section
file = sys.argv[1]
lines = list()

for line in open(file):
    line = line.rstrip('\n')
    lines.append(line)
rows = len(lines)
cols = len(lines[0])

hsh = defaultdict(list)
gears = set()
nums = list()
for lnum, line in enumerate(lines):
    in_num = False
    num = ''
    tmp = list()
    isValid = False
    for i, v in enumerate(line):
        if in_num:
            if v.isdigit():
                num += v
                if isAdjacent(lnum, i):
                    isValid = True
            else:
                #print(f'lnum, num, isValid = {lnum}, {num}, {isValid}')
                if isValid:
                    tmp.append(int(num))
                    for gear in gears:
                        hsh[gear] += [int(num)]
                isValid = False
                in_num = False
                num = ''
                gears = set()
        elif v.isdigit():
            in_num = True
            num += v
            if isAdjacent(lnum, i):
                isValid = True
    if len(num) > 0 and isValid:
        tmp.append(int(num))
        for gear in gears:
            hsh[gear] += [int(num)]
    nums.append(tmp)

res = 0
for item in nums:
    res += sum(item)
print(res)

#print(hsh)
ans2 = 0
for k, v in hsh.items():
    if len(v) == 2:
        ans2 += v[0] * v[1]

print(ans2)


