

def deep(bits):
    if len(bits)>1:
        if bits[0:2] == [1,0]:
            return deep(bits[2:])

        elif bits[0:2] == [1,1]:
            return deep(bits[2:])
        elif bits[0] == 0:
            return deep(bits[1:])

    elif len(bits)==1:
        if bits[0] == 0:
            return True
        else:
            return False
    else:
        return False

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        a=0
        while 1:
            print(a)
            if a < len(bits)-1:
                if bits[a]==1 and bits[a+1]==0:
                    a=a+2
                elif bits[a]==1 and bits[a+1]==1:
                    a=a+2
                elif bits[a]== 0:
                    a=a+1
            elif a == len(bits)-1:
                if bits[a]== 0:
                    return True
                else:
                    return False
            else:
                return False
           