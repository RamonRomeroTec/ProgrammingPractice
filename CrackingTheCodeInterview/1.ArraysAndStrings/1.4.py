'''

Palindrome Permutation: Given a string, write a function to check if it is
permutation of a palindrome. A palindrome is a word or phrase that is the same
 forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.
EXAMPLE
'''




'''


'''



#exponetial O(2^N)
#Itertool allows us to get all the conbinatios, we cana aso do this by ana recursive treeself.
#The prombem , is the space. With tree is 2^n but using the lib NLOGN



from itertools import permutations

def palin(s):
    s=s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False

def determine(a):
    a=list(permutations(a, len(a)))
    print(len(a))
    for w in a:
        a=''.join(w)
        if (palin(a)):

            return True
    return False


#O(2N), as we go thru all the Counter and the string

from collections import Counter

def palin3(s):
    setrep=Counter(s)
    o=0
    for k,v in setrep.items():
        if v%2==1:
            o=o+1
            if o>1:
                return False

    return True



# O(N)
def palin2(s):
    setrep=set()
    for i in s:
        if i in setrep:
            setrep.remove(i)

        else:
            setrep.add(i)

    if len(setrep)<=1 :
        return True
    else:
        return False










if __name__ == '__main__':
    a="aaabbaaa"
    #print(determine(a))
    print(palin2(a))
    print(palin3(a))
