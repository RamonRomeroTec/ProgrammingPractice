class Solution:
    def mostVisited(self, n, rounds):
        i=0
        arv={ x:0 for x in range(1,n+1)}
        c=rounds[0]
        while i<len(rounds)-1:
            if (c%n) ==  0:
                if rounds[i+1]==n:
                    i+=1
                arv[n]+=1
            else:
                if rounds[i+1]==(c%n):
                    i+=1
                arv[c%n]+=1
            c+=1
        k= max(arv.values())
        return [x[0] for x in sorted(arv.items(), key=lambda x:x[1], reverse=True) if x[1]==k]
            
                
                
                
            
        