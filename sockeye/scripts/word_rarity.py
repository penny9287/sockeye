import sys
import math
from collections import Counter

counter = Counter()
with open(sys.argv[1], "rt") as f:
    for line in f:
        line = line.rstrip().split()
        counter.update(line)

total = sum(counter.values())

scores = []
#lines = []
with open(sys.argv[1], "rt") as f:
    for line in f:
        line = line.rstrip()
        vec = line.split()
        scores.append(sum([-math.log(counter[w] / total) for w in vec]))

#max_val = max(scores)
max_val = 1

for s in scores:
    print(s / max_val)






