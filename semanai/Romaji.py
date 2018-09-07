
from sys import stdin
import pdb

vowels={'a','e','i','o','u'}

def fname(name):
    eval=True
    pdb.set_trace()
    if(name[-1]=='n' or name[-1] in vowels):
        for i in range(0, len(name)-1):
            if name[i] not in vowels:
                if name[i+1] in vowels:
                    eval=eval and True
                else:
                    eval=eval and False
                    break
            else:
                if name[i+1] in vowels:
                    eval=eval and True
                else:
                    eval=eval and False
                    break
                print(eval, name[i], name[i+1] )

        return eval


    else:
        return False


if __name__ == '__main__':
    name = str(input())
    if fname(name)==True:
        print ("YES")
    else:
        print ("NO")
