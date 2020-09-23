class Solution:
    def robotSim(self, commands,obstacles):
        obstacles = {(x[0],x[1]) for x in obstacles}
        state=0
        current=(0,0)
        euclid=0
      
        for c in commands:
            if c==-1: # right
                c=(c+1)%4
            elif c==-2:
                c=(c-1)%4
            else:
                if state==0:
                    for s in range(c):
                        current=(current[0], current[1]+1)
                        if current in obstacles:
                            current=(current[0], current[1]-1)
                            break
                        euclid=max(euclid, ((current[0]**2)+(current[1]**2)))
                elif state==1:
                    for s in range(c):
                        current=(current[0]+1, current[1])
                        if current in obstacles:
                            current=(current[0]-1, current[1])
                            break
                        euclid=max(euclid, ((current[0]**2)+(current[1]**2)))

                elif state==2:
                    for s in range(c):
                        current=(current[0], current[1]-1)
                        if current in obstacles:
                            current=(current[0], current[1]+1)
                            break
                        euclid=max(euclid, ((current[0]**2)+(current[1]**2)))

                else:
                    for s in range(c):
                        current=(current[0]-1, current[1])
                        if current in obstacles:
                            current=(current[0]+1, current[1])
                            break
                        euclid=max(euclid, ((current[0]**2)+(current[1]**2)))
        return euclid
        