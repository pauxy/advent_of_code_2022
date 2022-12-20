puz = open("puzzle").read()[:-1]
print([h for h in [ i + 14 if sum([puz[i:i+14].count(ii) for ii in puz[i:i+14]])==14 else None for i in range(len(puz)-13) ] if h!=None][0])
