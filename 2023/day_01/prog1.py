import sys
import re

file = sys.argv[1]
res = 0
for line in open(file):
    arr = re.findall(r'\d', line)
    #print(arr, arr[0], arr[-1], int(arr[0]+arr[-1]))
    res += int(arr[0]+arr[-1])

print(res)


