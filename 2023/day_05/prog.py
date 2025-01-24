import re
import sys

file = sys.argv[1]
seed_list = list()
sts_map = list()
stf_map = list()
ftw_map = list()
wtl_map = list()
ltt_map = list()
tth_map = list()
htl_map = list()

in_sts_map = False
in_stf_map = False
in_ftw_map = False
in_wtl_map = False
in_ltt_map = False
in_tth_map = False
in_htl_map = False

for line in open(file):
    line = line.rstrip('\n')
    if line.startswith('seeds:'):
        seed_list = [int(x) for x in re.sub(r'^seeds:\s+', r'', line).split()]
    elif line.startswith('seed-to-soil map:'):
        in_sts_map = True
    elif in_sts_map:
        if line == '':
            in_sts_map = False
        else:
            sts_map.append([int(x) for x in line.split()])
    elif line.startswith('soil-to-fertilizer map:'):
        in_stf_map = True
    elif in_stf_map:
        if line == '':
            in_stf_map = False
        else:
            stf_map.append([int(x) for x in line.split()])
    elif line.startswith('fertilizer-to-water map:'):
        in_ftw_map = True
    elif in_ftw_map:
        if line == '':
            in_ftw_map = False
        else:
            ftw_map.append([int(x) for x in line.split()])
    elif line.startswith('water-to-light map:'):
        in_wtl_map = True
    elif in_wtl_map:
        if line == '':
            in_wtl_map = False
        else:
            wtl_map.append([int(x) for x in line.split()])
    elif line.startswith('light-to-temperature map:'):
        in_ltt_map = True
    elif in_ltt_map:
        if line == '':
            in_ltt_map = False
        else:
            ltt_map.append([int(x) for x in line.split()])
    elif line.startswith('temperature-to-humidity map:'):
        in_tth_map = True
    elif in_tth_map:
        if line == '':
            in_tth_map = False
        else:
            tth_map.append([int(x) for x in line.split()])
    elif line.startswith('humidity-to-location map:'):
        in_htl_map = True
    elif in_htl_map:
        if line == '':
            in_htl_map = False
        else:
            htl_map.append([int(x) for x in line.split()])

# print('\nsts_map =>')
# print(sts_map)
# print('\nstf_map =>')
# print(stf_map)
# print('\nftw_map =>')
# print(ftw_map)
# print('\nwtl_map =>')
# print(wtl_map)
# print('\nltt_map =>')
# print(ltt_map)
# print('\ntth_map =>')
# print(tth_map)
# print('\nhtl_map =>')
# print(htl_map)

print(seed_list)

min_val = float('inf')

for seed in seed_list:
    print(f'seed = {seed}')
    soil = None
    for dst, src, size in sts_map:
        if src <= seed <= src + size:
            soil = seed - src + dst
            break
    if soil is None:
        soil = seed
    print(f'\tsoil        = {soil}')

    fertilizer = None
    for dst, src, size in stf_map:
        if src <= soil <= src + size:
            fertilizer = soil - src + dst
            break
    if fertilizer is None:
        fertilizer = soil
    print(f'\tfertilizer  = {fertilizer}')

    water = None
    for dst, src, size in ftw_map:
        if src <= fertilizer <= src + size:
            water = fertilizer - src + dst
            break
    if water is None:
        water = fertilizer
    print(f'\twater       = {water}')

    light = None
    for dst, src, size in wtl_map:
        if src <= water <= src + size:
            light = water - src + dst
            break
    if light is None:
        light = water
    print(f'\tlight       = {light}')

    temperature = None
    for dst, src, size in ltt_map:
        if src <= light <= src + size:
            temperature = light - src + dst
            break
    if temperature is None:
        temperature = light
    print(f'\ttemperature = {temperature}')

    humidity = None
    for dst, src, size in tth_map:
        if src <= temperature <= src + size:
            humidity = temperature - src + dst
            break
    if humidity is None:
        humidity = temperature
    print(f'\thumidity    = {humidity}')

    location = None
    for dst, src, size in htl_map:
        if src <= humidity <= src + size:
            location = humidity - src + dst
            break
    if location is None:
        location = humidity
    print(f'\tlocation    = {location}')
    min_val = min(min_val, location)
    print(f'\t\tmin_val = {min_val}')


print(min_val)


