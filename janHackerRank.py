//NOTE - Two Strings

//NOTE - given two arrays of strings, determine whether corresponding elements contain a common substring


def commonSubstring(a, b):

    for i in range(len(a)):
        s1 = set(a[i]).intersection(b[i])
        if len(s1):
            print("YES")
        else:
            print('NO')
