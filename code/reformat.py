class Solution:
    def reformat(self, s: str) -> str:
        letter = []
        nums = []
        ns=set([ str(x) for x in range(0,10)])
        for i in s:
            if i in ns:
                nums.append(i)
            else:
                letter.append(i)
        if not nums and len(letter)==1:
            return letter[0]
        elif not letter and len(nums)==1:
            return nums[0]
        elif ((not nums) and letter) or (nums and (not letter)):
            return ""
        elif not (len(nums)-len(letter))<=1:
            return ""
        else:
            ans=[]
            if len(nums)>len(letter):
                while True:
                    try:
                        ans.append(nums.pop())
                        ans.append(letter.pop())
                    except:
                        pass
                    if not nums and not letter:
                        break
            else:
                while True:
                    try:
                        ans.append(letter.pop())
                        ans.append(nums.pop())
                    except:
                        pass
                    if not nums and not letter:
                        break
            return "".join(ans)
                
                        
        