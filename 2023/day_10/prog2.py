# Solution of user: "BradleySigma" in the following link:
# https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/?rdt=52488

import sys
input_file = sys.argv[1]

d, q, r, n = (lambda t: (t, {min((t[j].find("S"),j) for j in range(len(t)) if "S" in t[j])}, set(), -2))(open(input_file).read().strip().split())
while q or print(n, sum(sum(d[j][k] in "|JLS" for k in range(i) if (k,j) in r)%2 for j in range(len(d)) for i in range(len(d[j])) if (i,j) not in r)): r, q, n = r|q, {(u,v) for x,y in q-r for u,v,f,g in [(x+1, y, "-LFS", "-J7"), (x-1, y, "-J7S", "-LF"), (x, y+1, "|F7S", "|LJ"), (x, y-1, "|LJS", "|F7")] if 0 <= v < len(d) and 0 <= u < len(d[v]) and d[y][x] in f and d[v][u] in g}, n+1

