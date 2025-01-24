import sys

file = sys.argv[1]
res = 0
for line in open(file):
    line = line.rstrip('\n')
    nums = [int(x) for x in line.split()]
    res += nums[-1]
    #print(f'nums, res = {nums}, {res}')
    while not (len(set(nums)) == 1 and sum(nums) == 0):
        tmp = [nums[i]-nums[i-1] for i in range(1, len(nums))]
        res += tmp[-1]
        nums = tmp
        #print(f'\tnums, res = {nums}, {res}')

# 6590 : That's not the right answer; your answer is too low.
# 2175229206 : That's the right answer!
print(res)

# ===================
# Part 2
# ===================
res = 0
for line in open(file):
    line = line.rstrip('\n')
    nums = [int(x) for x in line.split()]
    res += nums[0]
    step = 0
    while not (len(set(nums)) == 1 and sum(nums) == 0):
        tmp = [nums[i]-nums[i-1] for i in range(1, len(nums))]
        step += 1
        if step % 2 == 1:
            res -= tmp[0]
        else:
            res += tmp[0]
        nums = tmp

print(res)


