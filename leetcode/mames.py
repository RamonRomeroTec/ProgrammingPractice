def ar(plants, cap1, cap2):
    can1 = 0
    can2 = 0
    lo = 0
    hi = len(plants) - 1
    numRefils = 0
    while (lo < hi):
        if (can1 < plants[lo]):
            can1 = cap1;
            numRefils+=1
        if (can2 < plants[hi]):
            can2 = cap2
            numRefils+=1
        lo+=1
        hi-=1

        can1 -= plants[lo]
        can2 -= plants[hi]
        
    if (lo == hi and (plants[lo] > can1 + can2)):
        return ++numRefils
    else: 
        return numRefils;

