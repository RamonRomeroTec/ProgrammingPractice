class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - 1 - i))
        return (int(i) for i in str(num+1))