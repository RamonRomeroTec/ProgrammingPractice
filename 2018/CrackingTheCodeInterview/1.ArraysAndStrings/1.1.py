'''
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
'''

# O(N^2) but no Data Structures, SpaceComplexity N
import timeit

def uniqueNoDS(s):
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if s[i]==s[j] and j !=i:
                return False
    return True


#O (N log N)

def uniqueNoDSSort(s):
    s=sorted(s)
    for i in range(0, len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True



# O(N) Data Structures, SpaceComplexity 2N

def uniqueDS(s):
    a=set(s)
    if len(a)==len(s):
        return True
    return False

if __name__ == '__main__':
    #s=str(input())


    print(uniqueDS(s))
    print(uniqueNoDS(s))
    print(uniqueNoDSSort(s))
