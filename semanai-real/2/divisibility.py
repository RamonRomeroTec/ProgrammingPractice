

def findDiv(div):
  for i in divs:
    if str(i) in div:
      return i
  return -1

if __name__ == '__main__':
    n = input()
    n = list(n)
    divs = [(8*(i)) for i in range(26)]
    can = -1

    #
    while (int(n[len(n)-1])%2 != 0 and len(n) > 2): n.pop()
    can = findDiv("".join(n))
    if (int("".join(n)) % 8 == 0):
      print("YES\n{}".format("".join(n)))
    elif (can != -1):
      print("YES\n{}".format(can))
    else:
      aux = []
      num = len(n)-1
      while (num > 0):
        aux = n[:]
        aux.pop(num)
        if (int("".join(aux)) % 8 == 0):
          can = "".join(aux)
          break
        else:
          can = findDiv("".join(aux))
          if (can != -1): break
        num-=1
      if (can != -1):
        print("YES \n{}".format(can))
      else:
        print("NO")
