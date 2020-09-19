class Solution:
    def magic(self, ns, current, trace):
        if ns in trace:
            return True
        else:
            current[0], current[1] = ns[0], ns[1]
            trace.add(ns)
            return False
    def isPathCrossing(self, path: str) -> bool:
        current=[0,0]
        trace={(0,0)}
        for l in path:
            if l == 'N':
                ns=(current[0], current[1]+1)
                if self.magic(ns, current, trace):
                    return True
            elif l=='S':
                ns=(current[0], current[1]-1)
                if self.magic(ns, current, trace):
                    return True
            elif l=='E':
                ns=(current[0]+1, current[1])
                if self.magic(ns, current, trace):
                    return True
            else:
                ns=(current[0]-1, current[1])
                if self.magic(ns, current, trace):
                    return True
        return False



                
        