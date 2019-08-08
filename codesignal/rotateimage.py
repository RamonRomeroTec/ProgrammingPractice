'''
You are given an n x n 2D matrix
that represents an image. Rotate
the image by 90 degrees (clockwise).
'''
def rotateImage(a):
    ans=[]
    s=len(a)
    for i in (range(s)):
        l=[]
        for j in reversed(range(s)):
            l.append(a[j][i])

        ans.append(l)
    return ans
