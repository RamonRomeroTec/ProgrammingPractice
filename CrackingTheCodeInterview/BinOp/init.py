def Add(x, y):
    print(bin(x), bin(y))

    # Iterate till there is no carry
    while (y != 0):

        # carry now contains common
        # set bits of x and y
        carry = x & y
        print(bin(carry))


        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y
        print(bin(x))



        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1
        print(bin(y))


    return x

print(Add(2, 3))
