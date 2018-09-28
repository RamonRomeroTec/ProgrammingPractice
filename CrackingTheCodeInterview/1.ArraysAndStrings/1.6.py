'''

 Implement a method to perform basic string compression using the counts of
 repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
 If the "compressed" string would not become smaller than the original string,
 your method should return the original string. You can assume the string has
 only uppercase and lowercase letters (a - z).

'''


#la aplicacion de un Counter
#para ordenar podemos utilizar la funcion lambda

from collections import Counter
def fun(s):
    a=Counter(s)
    l=[]
    for k,v in sorted(a.items(), key=lambda k: k):
        l.append(k)
        l.append(str(v))

    if not len(l)<len(s):
        return s
    else:
        return "".join(l)



def fun2(s):
    l={}
    s2=[]
    for i in s:
        if i in l.keys():
            l[i]=l[i]+1
        else:
            l[i]=1
    for k,v in l.items():
        s2.append(k)
        s2.append(str(v))

    if not len(s2)<len(s):
        return s
    else:
        return "".join(s2)


if __name__ == '__main__':
    a="aabbcc"
    print(fun(a))
    a="aabbccc"
    print(fun(a))
    a="aabbcc"
    print(fun2(a))
    a="aabbccc"
    print(fun2(a))
