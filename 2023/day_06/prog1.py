import sys
import re

def findNumberOfWays(t, d):
    # We use Binary Search to find out the range.
    left, right = 0, t
    while left <= right:
        mid = (left + right) // 2
        val = mid * (t - mid)
        if val > d:
            right = mid - 1
        else:
            left = mid + 1
    start = left
    left, right = 0, t
    while left <= right:
        mid = (left + right) // 2
        val = mid * (t - mid)
        if val > d:
            left = mid + 1
        else:
            right = mid - 1
    end = right
    return end - start + 1

# =======================
# Main section
# =======================
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
    cnt = findNumberOfWays(t, d)
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

ans = findNumberOfWays(total_time, total_distance)
print(ans)


