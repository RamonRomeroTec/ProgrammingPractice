def magic(num, dic):
    #print(num not in dic)
    if num not in dic:
        dic[num]= magic(num-1, dic) + magic(num-2, dic) + magic(num-3, dic)
        return dic[num]
    else:
        #print(dic[num])
        return dic[num]
    
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        d1={1:1, 2:1, 0:0}
        return magic(n, d1)
       
        