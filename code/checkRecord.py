class Solution(object):
    def checkRecord(self, s):
        a=0
        c=0
        for i in s:
            if i == 'A':
                c=0
                a+=1
                if a>1:
                    return False
            elif i == 'L':
                c+=1
                if c>2:
                    return False
            else:
                c=0
        return True
                
            
        