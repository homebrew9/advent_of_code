import sys
import pathlib

#logs_list = [
#     'result_1.log',
#     'result_2.log',
#     'result_3.log',
#     'result_4.log',
#     'result_5.log',
#     'result_6.log',
#     'result_7.log',
#     'result_8.log',
#     'result_9.log',
#     'result_10.log',
#]

file = sys.argv[1]
for line in open(file):
    line = line.rstrip('\n')
    if line.startswith('seeds:'):
        seed_list = [int(x) for x in line.replace('seeds:', '').strip().split()]

#print(seed_list)
hsh = dict()
ind = 1
for i in range(0, len(seed_list), 2):
    fname = f'result_{ind}.log'
    hsh[fname] = [seed_list[i], seed_list[i]+seed_list[i+1]-1, seed_list[i+1]]
    ind += 1

#print(hsh)

parent_folder = pathlib.Path(__file__).parent.absolute()
logs_list = list()
for file in parent_folder.glob('result*.log'):
    logs_list.append(file.name)

#hsh = dict()
min_val = float('inf')
max_elapsed_seconds = float('-inf')
max_elapsed_minutes = float('-inf')

for log in logs_list:
    tmp = list()
    for line in open(log):
        line = line.strip('\n')
        if line != '':
            tmp.append(line.split('=')[1].strip())
    tmp[-2] = round(float(tmp[-2]), 9)
    tmp.insert(len(tmp)-1, round(tmp[-2]/60, 9))
    hsh[log] += tmp
    min_val = min(min_val, int(tmp[-1]))
    max_elapsed_seconds = max(max_elapsed_seconds, tmp[-3])
    max_elapsed_minutes = max(max_elapsed_minutes, tmp[-2])

#print(hsh)
print('\n')
print('%15s %20s %20s %20s %20s %20s %20s %20s %20s'%('Log_File', 'Seed_From', 'Seed_To', 'Seed_Range', 'Start_Time', 'End_Time', 'Elapsed_Seconds', 'Elapsed_Minutes', 'Loc_Val'))
print('%15s %20s %20s %20s %20s %20s %20s %20s %20s'%('-'*15, '-'*20, '-'*20, '-'*20, '-'*20, '-'*20, '-'*20, '-'*20, '-'*20))
for k in sorted(hsh.keys(), key=lambda x: int(x.replace('result_','').replace('.log',''))):
    start_time, end_time, elapsed_seconds, elapsed_minutes, loc_val = '', '', '', '', ''
    log_file = k
    if len(hsh[k]) == 3:
        seed_from, seed_to, seed_range = hsh[k]
    else:
        seed_from, seed_to, seed_range, start_time, end_time, elapsed_seconds, elapsed_minutes, loc_val = hsh[k]
    print('%-15s %20s %20s %20s %20s %20s %20s %20s %20s'%(log_file, seed_from, seed_to, seed_range, start_time, end_time, elapsed_seconds, elapsed_minutes, loc_val))
print('\n===============')
print(f'Max elapsed time    = {max_elapsed_seconds} sec ~ {max_elapsed_minutes} min')
print(f'Overall loc min val = {min_val}')
print('===============\n')


