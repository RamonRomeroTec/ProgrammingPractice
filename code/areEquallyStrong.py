def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    mina=min(yourLeft, yourRight)
    maxa=max(yourLeft, yourRight)

    maxb=max(friendsLeft, friendsRight)
    minb=min(friendsLeft, friendsRight)

    return mina==minb and maxb==maxa
