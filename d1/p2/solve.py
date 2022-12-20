print(sum(sorted([eval(i) for i in "+".join(open("puzzle").readlines()).replace("\n","").split("++")])[-3:]))
