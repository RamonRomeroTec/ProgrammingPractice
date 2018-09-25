if __name__ == '__main__':
    s, v1, v2, t1, t2= map(int, input().split(' '))
    p1 = 2 * t1 + v1 * s
    p2 = 2 * t2 + v2 * s
    if (p1 == p2):
        print("Friendship")
    elif (p1 < p2):
        print("First")
    else:
        print("Second")
