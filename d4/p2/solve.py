import re
with open("puzzle","r") as f:
    print(sum([0 if set(range(ii[0],ii[1]+1))&set(range(ii[2],ii[3]+1)) == set() else 1 for ii in [[int(iii) for iii in re.split("[,-]",i.strip())] for i in f.readlines()]]))
