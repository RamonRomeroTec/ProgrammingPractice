class Solution:
    def twoSum(self, nums, target):
        s=sorted(nums)
        for i in range(0, len(s)-1):
            lf=target-s[i]
            try:
                a=(s[(i+1):].index(lf))+i-1
                print(lf,i,a)
                l=nums.index(s[i])
                r=nums.index(s[][a-i-1])
                return [l,r]
            except:
                pass




if __name__ == '__main__':
    a=[3,3]
    b=6

    a=[3,2,4]
    print(Solution().twoSum(a,b))
