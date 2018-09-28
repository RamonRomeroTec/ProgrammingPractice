'''

Rotate Matrix: Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes, write a method to rotate
the image by 90 degrees. (an you do this in place?
Hints: #51, #100


'''



##### -> reversed(range((len(arr[0])))):



import pprint

def rotateright(arr):
    m=[]
    for j in (range(len(arr))):
        l=[]
        for i in reversed(range((len(arr[0])))):
            l.append(arr[i][j])
        m.append(l)
    return m





if __name__ == '__main__':
    m=[[1, 2 ,3],
    [4, 5 ,6],
    [7, 8 ,9]]

    pprint.pprint (rotateright(m))
    pprint.pprint (m)
