with open("puzzle","r") as f:
    print(max([eval(i) for i in "+".join(f.read().split("\n")[:-1]).split("++")]))
