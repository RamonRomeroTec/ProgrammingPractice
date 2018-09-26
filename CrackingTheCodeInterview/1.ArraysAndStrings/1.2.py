'''

Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other.

'''
#O(1) < O(log n) < O(n) < O(n log n) < O(n^2)

#O (N^2)

'''
#DP Memoization (+T(N)),
itertools or iterative/recursive generation of the combinations
 + (hashing (set) or iterative)
'''


# O(n log n)

def checkPermutation(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    for i in range(0,len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True

# O(N)


from collections import Counter
def checkPermutation2(s1,s2):
    if len(s1)!=len(s2):
        return False
    a=Counter(s1)
    b=Counter(s2)
    for k,v in b.items():
        if k not in a:
            return False
        else:
            if v != a[k]:
                return False
    return True




#set intersection or counter intersection



if __name__ == '__main__':
    sa="abcd"
    sb="acde"
    print(checkPermutation(sa,sb))
    print(checkPermutation2(sa,sb))

    sa="aabcd"
    sb="abacd"
    print(checkPermutation(sa,sb))
    print(checkPermutation2(sa,sb))


    sa="aabcd"
    sb="abacd"
    print(checkPermutation(sa,sb))
    print(checkPermutation2(sa,sb))

    sa="aaaabcd"
    sb="abaascd"
    print(checkPermutation(sa,sb))
    print(checkPermutation2(sa,sb))
