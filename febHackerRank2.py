# NOTE - write function named longestCommonPrefix to find the longest common prefix string amongst an array of strings.  If there is no common prefix, return an empty string "".

def longestCommonPrefix(array):

    output = ""

    for x in range(len(array[0])):
        for y in range(1, len(array)):
            if x <= len(array[y]) - 1:
                if array[0][x] != array[y][x]:
                    return output
            else:
                return output
        output += array[0][x]
    return output
