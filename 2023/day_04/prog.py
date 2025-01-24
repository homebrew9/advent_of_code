import sys
import re
from collections import defaultdict

# Main section
file = sys.argv[1]
p1 = 0
hsh = defaultdict(list)

for line in open(file):
    line = line.rstrip('\n')
    card = int(re.split(r'[:|]', line)[0].replace('Card','').strip())
    arr = re.split(r'[:|]', line)
    wins = set([int(x) for x in re.split(r'[:|]', line)[1].split()])
    haves = [int(x) for x in re.split(r'[:|]', line)[2].split()]
    cnt = 0
    for have in haves:
        if have in wins:
            cnt += 1
    if cnt > 0:
        p1 += 2**(cnt-1)
    hsh[card] = [1, cnt]

print(p1)

#   #print(hsh)
#   max_val = max(hsh.keys())
#   p2 = 0
#   #print(max_val)
#   for k in sorted(hsh.keys()):
#       instances, wins = hsh[k]
#       p2 += instances
#       for _ in range(instances):
#           if wins > 0:
#               for key in range(k+1, min(k+wins+1, max_val+1)):
#                   hsh[key][0] += 1
#       #print('==========')
#       #print(hsh)
#   
#   #print('##########')
#   #print(hsh)
#   
#   #p2 = 0
#   #for k in sorted(hsh.keys()):
#   #    p2 += hsh[k][0]
#   
#   print(p2)

# =================================
# Optimized Part 2
# =================================
max_val = max(hsh.keys())
p2 = 0
for k in sorted(hsh.keys()):
    instances, wins = hsh[k]
    p2 += instances
    for j in range(wins):
        hsh[k+1+j][0] += hsh[k][0]

print(p2)


