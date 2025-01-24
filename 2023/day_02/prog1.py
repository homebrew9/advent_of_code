import sys
import re

file = sys.argv[1]
res = 0
actual = {'red': 12, 'green': 13, 'blue': 14}

for line in open(file):
    line = line.rstrip('\n')
    game = int(re.sub(r'^Game\s+(\d+):.*$', r'\1', line))
    red_grab = [int(x.replace(' red','')) for x in re.findall('\d+ red', line)]
    if max(red_grab) > actual['red']:
        continue
    green_grab = [int(x.replace(' green','')) for x in re.findall('\d+ green', line)]
    if max(green_grab) > actual['green']:
        continue
    blue_grab = [int(x.replace(' blue','')) for x in re.findall('\d+ blue', line)]
    if max(blue_grab) > actual['blue']:
        continue
    res += game

print(res)

