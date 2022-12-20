print(max([eval(i) for i in "+".join(open("puzzle").read().split("\n")[:-1]).split("++")]))
