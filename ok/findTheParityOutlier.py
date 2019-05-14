def find_outlier(integers):
    odd = 0
    even = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            even = even+1
        else:
            odd = odd+1
        if even == 2:
            for j in range(len(integers)):
                if integers[j] % 2 == 1:
                    return integers[j]

        if odd == 2:
            for j in range(len(integers)):
                if integers[j] % 2 == 0:
                    return integers[j]
