'''
Note: Uso de sets para minimizar memoria y 
fraccion de integers -> Digitos 
while(i>=10):
    ds=set
    while(i >= 10):
        d=i%10
        if d==0:
            adition=False
            break
        ds.add(d)
        i=i/10
    ds.add(i)

'''


class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []
        for i in range(left, right+1):
            original = i
            ds = set()
            adition = True
            while(i >= 10):
                d = i % 10
                if d == 0:
                    adition = False
                    break
                ds.add(d)
                i = i/10
            ds.add(i)
            if adition == True:
                for i in ds:
                    if original % i != 0:
                        adition = False
                        break
            if adition == True:
                ans.append(original)

        return ans
