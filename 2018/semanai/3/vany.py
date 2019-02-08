'''
4
0 0
1 1
2 0
2 2
'''
from cmath import phase

if __name__ == '__main__':

    n = int(raw_input())
    a = [map(int, raw_input().split()) for i in xrange(n)]
    arr = [complex(x[0], x[1]) for x in a]
    res = 0
    for i in xrange(n):
        arr1 = []
        for j in xrange(i):
            if a[i] == a[j]:
                res += n - 2
            elif a[j][0] < a[i][0]:
                arr1.append(phase(arr[i] - arr[j]))
            elif a[j][0] > a[i][0]:
                arr1.append(phase(arr[j] - arr[i]))
            elif a[j][1] > a[i][1]:
                arr1.append(phase(arr[i] - arr[j]))
            else:
                arr1.append(phase(arr[j] - arr[i]))
        arr1.sort()
        p = -100
        cnt = 0
        for x in arr1:
            if x - p < 1e-9:
                cnt += 1
            else:
                cnt = 0
                p = x
            res += cnt
    print n * (n - 1) * (n - 2) / 6 - res
