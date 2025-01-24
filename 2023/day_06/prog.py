import sys
import re

file = sys.argv[1]

for line in open(file):
    line = line.rstrip('\n')
    if line.startswith('Time'):
        time_arr = [int(x) for x in re.sub(r'Time:', r'', line).split()]
    elif line.startswith('Distance'):
        distance_arr = [int(x) for x in re.sub(r'Distance:', r'', line).split()]

#print(time_arr)
#print(distance_arr)

res = 1
for t, d in zip(time_arr, distance_arr):
    cnt = 0
    for i in range(1, t):
        if i * (t - i) > d:
            cnt += 1
    res *= cnt

print(res)

# ============================
# Part 2
# ============================

total_time = ''.join([str(x) for x in time_arr])
total_distance = ''.join([str(x) for x in distance_arr])

total_time = int(total_time)
total_distance = int(total_distance)

#print(total_time)
#print(total_distance)

ans = 0
for i in range(1, total_time):
    if i * (total_time - i) > total_distance:
        ans += 1

print(ans)

