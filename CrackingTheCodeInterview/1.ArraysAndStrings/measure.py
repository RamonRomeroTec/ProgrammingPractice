# importing the required modules
import timeit

# binary search function

def uniqueDS(s):
    a=set(s)
    if len(a)==len(s):
        return True
    return False

# O(N^2) but no Data Structures, SpaceComplexity N

def uniqueNoDS(s):
    s=sorted(s)
    for i in range(0, len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True

def uniqueNoDSSort(s):
    s=sorted(s)
    for i in range(0, len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True

# compute binary search time
def uniqueNoDS_time():
    SETUP_CODE = '''
from __main__ import uniqueNoDS
from random import randint'''

    TEST_CODE = '''
mylist = [x for x in range(10000)]
uniqueNoDS(mylist)'''

    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)

    # priniting minimum exec. time
    print('Binary search time: {}'.format(min(times)))

if __name__ == "__main__":
    uniqueNoDS_time()
