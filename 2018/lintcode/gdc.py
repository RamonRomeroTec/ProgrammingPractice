

def okgdc(a,b):
    if b==a:
        return a
    if b>a:
        return okgdc(b,a)
    else:
        return okgdc(a-b, b)



class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        return okgdc(a,b)

        # write your code here
