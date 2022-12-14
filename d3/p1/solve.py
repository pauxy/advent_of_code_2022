with open("puzzle","r") as f:
    print(sum([[ ord(ii)-96 if ii>="a" else (ord(ii)-64)+26 for ii in i[:len(i)//2] if ii in i[len(i)//2:]][0] for i in f.readlines()]))
