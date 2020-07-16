class Solution:
    def average(self, salary):
        maxi=float('-inf')
        mini=float('+inf')
        s=0
        for n in salary:
            if n>maxi:
                maxi=n
            if n<mini:
                mini=n
            s+=n
        return (s-mini-maxi)/ (len(salary)-2)