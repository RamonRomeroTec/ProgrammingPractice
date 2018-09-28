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

'''




def oneWay(s,l):

    if ""==s and l=="":
        return False

    if s==l:
        return False
    if len(l)==len(s) or abs(len(l)-len(s))==1:

        k=min(len(s), len(l))
        i=0
        j=0
        c=0
        while(1):
            if  s[i] != l[j]:
                if s[i+1]==l[j]:
                    i=i+1

                elif s[i]==l[j+1]:
                    j=j+1

                c=c+1
                if c>1:
                    return False


            j=j+1
            i=i+1
            if i==len(s)-1 or j==len(l)-1:
                return True


    else:
        return False

if __name__ == '__main__':
    #print(oneWay("pale", "pae"))
    #print(oneWay("pales", "pale"))
    #print(oneWay("pale", "bale"))
    #print(oneWay("pale", "bake"))
    print(oneWay("pale", "ale"))
