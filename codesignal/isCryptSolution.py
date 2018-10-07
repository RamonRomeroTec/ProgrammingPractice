'''


A cryptarithm is a mathematical puzzle for which the goal is to find
the correspondence between letters and digits, such that the given
arithmetic equation consisting of letters holds true when the letters
are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array
containing the mapping of letters and digits, solution. The array
crypt will contain three non-empty strings that follow the structure:
[word1, word2, word3], which should be interpreted
as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the
cryptarithm with digits using the mapping in solution, becomes a valid
arithmetic equation containing no numbers with leading zeroes,
the answer is true. If it does not become a valid arithmetic solution,
the answer is false.



'''


def toMag(solution):
    d={}
    for i in solution:
        d[i[0]]=i[1]

    return d



def isCryptSolution(crypt, solution):
    d=toMag(solution)
    w1=[]
    for i in crypt[0]:
        n=d[i]
        w1.append(n)
    i1=("".join(w1))

    w2=[]
    for i in crypt[1]:
        n=d[i]
        w2.append(n)
    i2=("".join(w2))



    w3=[]
    for i in crypt[2]:
        n=d[i]
        w3.append(n)
    i3=("".join(w3))


    if (i1[0]=='0' or i2[0]=='0' or i3[0]=='0') and (len(i3)>1):
        return False

    return int(i1)+int(i2)==int(i3)
