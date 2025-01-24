import sys

file = sys.argv[1]
res = 0
nums = ['one','two','three','four','five','six','seven','eight','nine']
for line in open(file):
    line = line.rstrip('\n')
    arr = list()
    for i in range(len(line)):
        if line[i].isdigit():
            arr.append(int(line[i]))
        else:
            for j, num in enumerate(nums):
                if line[i:].startswith(num):
                    arr.append(j+1)
    res += (arr[0]*10 + arr[-1])

print(res)



