class Solution(object):
    def isLongPressedName(self, name, typed):
        if name==typed:
            return True
        i=0
        j=0
        c=0
        current=0
        while j<len(name):
            if name[i]==name[j]:
                c+=1
                j+=1
            else:
                partialc=0
                for k in range(current, len(typed)):
                    if typed[k]==name[i]:
                        partialc+=1
                    else:
                        if partialc < c:
                            return False
                        else:
                            current=k
                            break
                
                i=j
                c=0
            if j==len(name):
                c=1
                partialc=0
                for k in range(current, len(typed)):
                    if typed[k]==name[i]:
                        partialc+=1
                    else:
                        if partialc < c:
                            return False
                        else:
                            current=k
                            break
                i=j
        if typed[current]!=name[-1]:
            return False
        return True


                
                