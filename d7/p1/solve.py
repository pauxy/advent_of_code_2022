ALL ={}
current = ""
aa=lambda a: "/".join(current.split("/")[:-1 ]) if ".." in a else f"{current}/{a.strip().split(' ')[-1]}"
[globals().update(current=aa(i)) or ALL.setdefault(current,0) if i.startswith("$ cd")  else ALL.update({current:int(i.split(' ')[0])+ALL[current]}) for i in open("puzzle").readlines() if not (i.startswith('$ ls') or i.startswith('dir'))]
[[ALL.update({i:ALL[i]+ALL[ii]}) for ii in sorted(ALL.keys()) if ii.startswith(i) and ii!=i ]for i in sorted(ALL.keys())]
print(sum([ALL[i] for i in ALL.keys() if ALL[i]<=100000]))
