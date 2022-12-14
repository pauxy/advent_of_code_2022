with open("puzzle","r") as f:
    n = f.readlines()
    print(sum([[ ord(ii)-96 if ii>="a" else (ord(ii)-64)+26 for ii in n[i] if ii in n[i+1] and ii in n[i+2]][0] for i in range(0, len(n), 3)]))
