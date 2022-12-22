aa = lambda o,c,all: True if o[0]+c[0]>=len(all) or o[1]+c[1]>=len(all[0]) or o[0]+c[0]<0 or o[1]+c[1]<0  else aa(o,[ 0 if num==0 else num-1 if num<0 else num+1 for num in c],all) if  all[o[0]][o[1]]>all[o[0]+c[0]][o[1]+c[1]]  else False
ALL =[i.strip() for i in open("puzzle").readlines()]
print(sum([ sum([ 1 if aa([x,y],[0,1],ALL) or aa([x,y],[1,0],ALL) or aa([x,y],[0,-1],ALL) or aa([x,y],[-1,0],ALL) else 0 for y in range(len(i))])for x,i in enumerate(ALL)]))

