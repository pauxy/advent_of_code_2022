P={}
a = lambda i: i.strip().split(" ")
with open("puzzle","r") as f:
    [[P[int(((c-1)/4)+1)].append(ii) if int(((c-1)/4)+1) in P.keys() else P.setdefault(int(((c-1)/4)+1),[ii]) for c,ii in enumerate(i) if ((c-1)/4)+1 in range(0,100) and ii!=" "] if (i[0] == "[" or i[0]==" " and i[1]!="1") else [ P[int(a(i)[5])].insert(0,P[int(a(i)[3])].pop(0)) for aa in range(int(a(i)[1]))] for i in f.readlines() if not (i.strip()=="" or i.startswith(" 1"))]
    print("".join([P[i][0] for i in sorted(P.keys())]))
