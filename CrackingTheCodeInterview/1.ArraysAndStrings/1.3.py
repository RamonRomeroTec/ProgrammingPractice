'''

URLify: Write a method to replace all spaces in a string with '%20:
You may assume that the string has sufficient space at the end to hold the
additional characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

'''

#find O(N) on average, O(NM) worst case (N being the length of the longer string
# M, the shorter string you search for).

#O(NLOGN)

def URLify(s, n):
    while (s.find(" ")>=0):
        x=s.find(" ")
        H=s[:x]
        T=s[x+1:]
        s=H+"%20"+T

    return s


#reduce time complexity but increase space complexity
#simplest solution

def URLify2(s, n):
    a=[]
    for i in range(0, len(s)):
        if s[i] == ' ':
            a.append("%20")
        else:
            a.append(s[i])
    return "".join(a)


    return s

#simplest

def URLify3(s, n):
    s=s.replace(" ", "%20")
    return s

if __name__ == '__main__':
    s="mr cringe es l"
    print(URLify(s,len(s)))
    print(URLify2(s,len(s)))
    print(URLify3(s,len(s)))
