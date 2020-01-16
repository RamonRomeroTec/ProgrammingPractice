class Solution(object):
    def isValid(self, s):
        stack=[]
        d={'(':')','[':']', '{':'}'}
        for i in s:
            if i in d:
                stack.append(i)
            else:
                try:
                    ev=stack[-1]
                except:
                    return False
                if d[ev]==i:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
            
            