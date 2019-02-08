'''
String Rotation: Assume you have amethod isSubstring which checks ifone
word is asubstring of another. Given two strings, 51 and 52, write code to
check if 52 is a rotation of 51 using only one call to isSubstring
(e.g.,"waterbottle"is a rotation of"erbottlewat").


'''



### UNA  ROTACION NO ES MAS QUE UN SEGMENTO CORTADO


def isrotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=s1+s1
    if s1.find(s2)>0:
        return True

if __name__ == '__main__':
    s1="waterbottle"
    s2="erbottlewat"

    print(isrotation(s1, s2))
