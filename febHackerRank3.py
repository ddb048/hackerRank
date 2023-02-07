# NOTE - Create a function called malarkeySort, it will be gien an n-length array of unsorted numbers, it shall sort them in the following manner: largest, smallest, 2nd largest, 2nd smallest, etc.

def malarkeySort(array):
    returnList = []

    high = None

    while array:
        smallest = min(array)
        largest = max(array)

        if len(array) > 0:
            low = array.pop(array.index(smallest))
            if len(array) > 0:
                high = array.pop(array.index(largest))

                returnList.append(high)
                returnList.append(low)

            else:
                returnList.append(low)

    return returnList
