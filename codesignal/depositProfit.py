def depositProfit(deposit, rate, threshold):
    c=0

    while deposit<threshold:
        c=c+1
        deposit=deposit*(1+rate/100)

    return c
