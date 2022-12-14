k = [2,0,1]

def calc(i):
    return [ii for ii in range(3) if k[(ii+2)%3-(i[0]-65)]==(i[1]-88)][0]+1+((i[1]-88)*3)
with open("puzzle","r") as f:
    print(sum([calc([ord(ii) for ii in i.strip().split()]) for i in f.readlines()]))
