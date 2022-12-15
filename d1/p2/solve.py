with open("puzzle","r") as f:
    print(sum(sorted([eval(i) for i in "+".join(f.readlines()).replace("\n","").split("++")])[-3:]))
