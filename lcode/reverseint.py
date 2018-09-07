class Solution():

    def reverse(self,x):
        pos=1
        s=str(x)
        s=(s[::-1])
        if s[-1]=='-':
            s=s[0:len(s)-1]
            pos=-1


        f=int(s)
        f=f*pos






        if (f<-2147483648 or f>2147483648 ):
        	 return 0
        else:
            return f

if __name__ == '__main__':
    x=-99999
    s=Solution()
    print(s.reverse(x))
