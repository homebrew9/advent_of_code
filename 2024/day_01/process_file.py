import sys
from collections import Counter

input_file = sys.argv[1]

arr1, arr2 = list(), list()

for line in open(input_file):
    elem1, elem2 = [int(i) for i in line.split()]
    arr1.append(elem1)
    arr2.append(elem2)

#print(len(arr1), arr1)
#print(len(arr2), arr2)

arr1.sort()
arr2.sort()

total = 0
for x, y in zip(arr1, arr2):
    total += abs(x - y)

print(total)

# ===============
# Part 2
# ===============

cntr = Counter(arr2)
score = 0
for n in arr1:
    score += n * cntr[n] if n in cntr else 0

print(score)


