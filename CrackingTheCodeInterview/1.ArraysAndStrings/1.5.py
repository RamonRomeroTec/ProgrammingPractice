'''

One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away.
EXAMPLE
pale, pIe -> true
pales.pale -> true
pale. bale -> true
pale. bake -> false


def oneWay(s,l):
    if len(l)==len(s):
        if s==l:
            return True
    else len(l)==len(s)+1:
        for i :
            pass

    elif len(l)==len(s)-1:

    else:
        return False
'''

def oneWay(s,l):
    if len(l)==len(s) or abs(len(l)-len(s))==1:

        k=min(len(s), len(l))
        i=0
        c=0
        for i in range(0,k):
            if  s[i] != l[i]:
                #print(s[i] ,l[i])
                c=c+1
            if c>1:
                return False

        return True
    else:
        return False


if __name__ == '__main__':
    print(oneWay("pale", "pae"))
    print(oneWay("pales", "pale"))
    print(oneWay("pale", "bale"))
    print(oneWay("pale", "bake"))
