if __name__ == '__main__':
    xhome, yhome = [int(x) for x in input().split()]
    xuni, yuni = [int(x) for x in input().split()]
    n_roads = int(input())
    n_steps = 0
    for i in range(n_roads):
        a, b, c = [int(x) for x in input().split()]
        hline = (a*xhome) + (b*yhome) + c
        uline = (a*xuni) + (b*yuni) + c
        if hline * uline < 0:
            n_steps += 1
    print(n_steps)
