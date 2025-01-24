import sys
from collections import deque

file = sys.argv[1]
res = 0
mat = list()
row, r, c = 0, 0, 0
for line in open(file):
    line = line.rstrip('\n')
    tmp = list()
    for i, ch in enumerate(line):
        if ch == 'S':
            r = row
            c = i
        tmp.append(ch)
    mat.append(tmp)
    row += 1

#print(f'S is at (r, c) = ({r}, {c})')
#print(mat)

rows = len(mat)
cols = len(mat[0])

r0, c0 = r, c

dq = deque()
seen = set()
dq.append((r, c))
seen.add((r, c))
steps = 0
max_val = float('-inf')
directions = [[-1,0],[0,1],[1,0],[0,-1]]
hsh = { ('F', (0,1)) : ['-', '7', 'J'],
        ('F', (1,0)) : ['|', 'J','L'],
        ('F', (0,-1)): [],
        ('F', (-1,0)): [],

        ('J', (-1,0)): ['F', '|', '7'],
        ('J', (0,-1)): ['-', 'F','L'],
        ('J', (1,0)) : [],
        ('J', (0,1)) : [],

        ('L', (-1,0)): ['F', '|', '7'],
        ('L', (0,-1)): [],
        ('L', (1,0)) : [],
        ('L', (0,1)) : ['-','7','J'],

        ('7', (-1,0)): [],
        ('7', (0,-1)): ['-','F','L'],
        ('7', (1,0)) : ['|','J','L'],
        ('7', (0,1)) : [],

        ('-', (0,1)) : ['-', 'J','7'],
        ('-', (0,-1)): ['-', 'F', 'L'],
        ('-', (1,0)) : [],
        ('-', (-1,0)): [],

        ('|', (-1,0)): ['|', 'F','7'],
        ('|', (1,0)) : ['|', 'J', 'L'],
        ('|', (0,1)) : [],
        ('|', (0,-1)): [],

        ('S', (-1,0)): ['|', 'F'],
        ('S', (0,1)) : ['-', 'J'],
        ('S', (1,0)) : ['|', 'J', 'L'],
        ('S', (0,-1)): ['-', 'F'],
      }
while dq:
    print(f'\tdq, steps, max_val = {dq}, {steps}, {max_val}')
    size = len(dq)
    for _ in range(size):
        r, c = dq.popleft()
        if r == r0 and c == c0:
            if 0 <= r-1 < rows and 0 <= r+1 < rows and mat[r-1][c] in ('|','7','F') and mat[r+1][c] in ('|','L','J'):
                # S is "|"
                dq.append((r-1,c)) ; dq.append((r+1,c))
                seen.add((r-1,c)) ; seen.add((r+1,c))
            elif 0 <= c+1 < cols and 0 <= c-1 < cols and mat[r][c+1] in ('-','F','L') and mat[r][c-1] in ('-','J','7'):
                # S is "-"
                dq.append((r,c+1)) ; dq.append((r,c-1))
                seen.add((r,c+1)) ; seen.add((r,c-1))
            elif 0 <= r-1 < rows and 0 <= c+1 < cols and mat[r-1][c] in ('|','7','F') and mat[r][c+1] in ('-','J','7'):
                # S is "L"
                dq.append((r-1,c)) ; dq.append((r,c+1))
                seen.add((r-1,c)) ; seen.add((r,c+1))
            elif 0 <= r-1 < rows and 0 <= c-1 < cols and mat[r-1][c] in ('|','7','F') and mat[r][c-1] in ('-','L','F'):
                # S is "J"
                dq.append((r-1,c)) ; dq.append((r,c-1))
                seen.add((r-1,c)) ; seen.add((r,c-1))
            elif 0 <= c-1 < cols and 0 <= r+1 < rows and mat[r][c-1] in ('-','L','F') and mat[r+1][c] in ('|','L','J'):
                # S is "7"
                dq.append((r,c-1)) ; dq.append((r+1,c))
                seen.add((r,c-1)) ; seen.add((r+1,c))
            elif 0 <= c+1 < cols and 0 <= r+1 < rows and mat[r][c+1] in ('-','J','7') and mat[r+1][c] in ('|','L','J'):
                # S is "F"
                dq.append((r,c+1)) ; dq.append((r+1,c))
                seen.add((r,c+1)) ; seen.add((r+1,c))
            continue
        for dr, dc in directions:
            rnew = r + dr
            cnew = c + dc
            if 0 <= rnew < rows and 0 <= cnew < cols:
                if mat[rnew][cnew] != '.' and (rnew, cnew) not in seen and mat[rnew][cnew] in hsh[(mat[r][c], (dr, dc))]:
                    dq.append((rnew, cnew))
                    seen.add((rnew, cnew))
    steps += 1
    max_val = max(max_val, steps)

print(max_val-1)


