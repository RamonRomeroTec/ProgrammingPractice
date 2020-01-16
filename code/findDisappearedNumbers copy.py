'''
ok
'''
import sort
class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):

        answ=set(nums)
        gen=set()

        for x in range(1, len(nums)+1):
            gen.add(x)
        #print (answ)
        #print (gen)
        a = gen-answ
        return sort(list(a))


if __name__ == '__main__':


    q=[10,2,5,10,9,1,1,4,3,7]




    s=Solution()

    print(str(s.findDisappearedNumbers(q)))
