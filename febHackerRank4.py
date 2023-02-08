# NOTE - Simple Max Difference

# NOTE - determine the max positive spread for a sotck given its price history.  If the stock remains flat or declines for the full period, return -1.

def maxDifference(array):
    possibleHighest = [-1]

    for x in array:
        for y in array:
            if y > x:
                possibleHighest.append(y - x)

# loop through the array in double nested
# in i, j, if j is > i, push difference into possibleHighest
# return max of possibleHighest
