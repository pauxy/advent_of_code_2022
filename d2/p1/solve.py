k = [6,0,3]
calc = lambda i:(k[(i[1]-86)%3-(i[0]-65)])+i[1]-87
print(sum([calc([ord(ii) for ii in i.strip().split()]) for i in open("puzzle").readlines()]))
