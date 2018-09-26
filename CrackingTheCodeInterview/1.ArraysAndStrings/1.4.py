'''

Palindrome Permutation: Given a string, write a function to check if it is
permutation of a palindrome. A palindrome is a word or phrase that is the same
 forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.
EXAMPLE
'''
from itertools import permutations
def palin(s):
    s=s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False

def determine(a):
    a=list(permutations(a, len(a)))
    for w in a:
        a=''.join(w)
        if (palin(a)):
            print(a)
            return("True")
    return False


if __name__ == '__main__':
    a="tact coa"
    print(determine(a))
