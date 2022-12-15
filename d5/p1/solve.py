P={}
with open("puzzle","r") as f:
    [[P[int(((c-1)/4)+1)].append(ii) if int(((c-1)/4)+1) in P.keys() else P.setdefault(int(((c-1)/4)+1),[ii]) for c,ii in enumerate(i) if ((c-1)/4)+1 in range(0,100) and ii!=" "]for i in f.readlines() if i[0] == "[" or i[0]==" " and i[1]!="1"]
    print(P)
