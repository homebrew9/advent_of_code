import sys
import re
from collections import defaultdict

D = open(sys.argv[1]).read().strip()
lines = D.split('\n')
ans = 0
N = defaultdict(int)

print(N)
for i, line in enumerate(lines):
    N[i] += 1
    print(f'\tN = {N}')
    first, rest = line.split('|')
    id_, card = first.split(':')
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    if val > 0:
        ans += 2**(val-1)
    for j in range(val):
        N[i+1+j] += N[i]
        print(f'\t\tj = {j}; N = {N}')
    print('============')
    print(N)

print('############')
print(N)

#print(ans)
print(sum(N.values()))

