puz = open("puzzle").read()[:-1]
print([h for h in [ i + 4 if sum([puz[i:i+4].count(ii) for ii in puz[i:i+4]])==4 else None for i in range(len(puz)-3) ] if h!=None][0])
