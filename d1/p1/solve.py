all = []
with open("puzzle","r") as f:
     print(max([eval(i) for i in "+".join(f.readlines()).replace("\n","").split("++")]))

