# NOTE - Simple Max Difference

# NOTE - determine the max positive spread for a sotck given its price history.  If the stock remains flat or declines for the full period, return -1.

def maxDifference(a):
    vmin = a[0]
    dmax = 0

    for i in range(len(a)):
        if (a[i] < vmin):
            vmin = a[i]
        elif (a[i] - vmin > dmax):
            dmax = a[i] - vmin

    if dmax == 0:
        dmax = -1
    return dmax


# loop through the array in double nested
# in i, j, if j is > i, push difference into possibleHighest
# return max of possibleHighest
