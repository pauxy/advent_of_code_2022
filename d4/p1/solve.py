import re
with open("puzzle","r") as f:
    print(sum([1 if (ii[0]>=ii[2] and ii[1]<=ii[3])or(ii[2]>=ii[0] and ii[3]<=ii[1]) else 0 for ii in [[int(iii) for iii in re.split("[,-]",i.strip())] for i in f.readlines()]]))
