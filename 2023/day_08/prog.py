import sys
import re
from collections import defaultdict

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

print(directions)
print(hsh)

#  N = len(directions)
#  pos = 0
#  curr_node = 'AAA'
#  end_node = 'ZZZ'
#  
#  dir = {'L': 0, 'R': 1}
#  curr_node = hsh[curr_node][dir[directions[pos]]]
#  print(curr_node)
#  distance = 1
#  
#  while curr_node != end_node:
#      pos = (pos + 1) % N
#      curr_node = hsh[curr_node][dir[directions[pos]]]
#      distance += 1
#  
#  print(distance) 

# =======================
# Part 2
# =======================

curr_nodes = list()
for k in hsh.keys():
    if k.endswith('A'):
        curr_nodes.append(k)

print(curr_nodes)

N = len(directions)
pos = 0

tmp = list()
for node in curr_nodes:
    nextNode = hsh[node][dir[directions[pos]]]
    tmp.append(nextNode)
curr_nodes = tmp
dist = 1
#print(curr_nodes)

ends = set([x[-1] for x in curr_nodes])
while not(len(ends) == 1 and list(ends)[0] == 'Z'):
    #print(f'\tcurr_nodes, dist, ends = {curr_nodes}, {dist}, {ends}')
    pos = (pos + 1) % N
    tmp = list()
    for node in curr_nodes:
        nextNode = hsh[node][dir[directions[pos]]]
        tmp.append(nextNode)
    curr_nodes = tmp
    dist += 1
    ends = set([x[-1] for x in curr_nodes])

print(dist)


