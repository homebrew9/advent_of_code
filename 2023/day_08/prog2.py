import math
import sys
import re
from collections import defaultdict

def cycleLength(node):
    pos = 0
    steps = 0
    while not node.endswith('Z'):
        print(f'\tnode, steps = {node}, {steps}')
        node = hsh[node][dir[directions[pos]]]
        steps += 1
        pos = (pos + 1) % N
    return steps

# ============================
# Main section
# ============================

file = sys.argv[1]
first_line = True
hsh = defaultdict(list)

for line in open(file):
    line = line.rstrip('\n')
    if first_line:
        directions = line
        first_line = False
    elif line.find('=') != -1:
        arr = re.findall(r'[0-9A-Z]+', line)
        hsh[arr[0]] = [arr[1], arr[2]]

#print(directions)
#print(hsh)

# =======================
# Part 2
# =======================

curr_nodes = list()
for k in hsh.keys():
    if k.endswith('A'):
        curr_nodes.append(k)

#print(curr_nodes)

N = len(directions)
dir = {'L': 0, 'R': 1}

res = None
for i, v in enumerate(curr_nodes):
    print('==========')
    if i == 0:
        res = cycleLength(v)
    else:
        res = math.lcm(res, cycleLength(v))

print(res)


