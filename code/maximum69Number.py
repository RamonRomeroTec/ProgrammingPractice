class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        a= s.find('6')
        if a != -1:
            return int(s[:a]+'9'+s[a+1:])
        else:
            return num
        
