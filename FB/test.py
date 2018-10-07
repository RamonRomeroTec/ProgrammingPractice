

def bulbs(A):
    state= 0
    ans = 0
    for i in range(len(A)):
        if (A[i] == state):
            ans=ans+1
            state = 1 - state
    return ans

if __name__ == '__main__':
    A=[0,1, 0, 1]
    print (bulbs(A))
