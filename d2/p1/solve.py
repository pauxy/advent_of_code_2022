k = [6,0,3]

def calc(i):
    return (k[(i[1]-86)%3-(i[0]-65)])+i[1]-87
with open("puzzle","r") as f:
    print(sum([calc([ord(ii) for ii in i.strip().split()]) for i in f.readlines()]))
