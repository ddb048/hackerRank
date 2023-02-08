
# NOTE - reverse_parentheses  given a string that consists of lower case english letters and brackets

# reverse the strings in each pair of matching parentheses starting from the innermost one

def reverse_parentheses(s):

    stack = []
    reverse = []

    for x in range(len(s)):

        if s[x] == ")":
            p = stack.pop()
            while p != "(":
                reverse.append(p)
                p = stack.pop()
            stack += reverse
            reverse = []
        else:
            stack.append(s[x])
    return "".join(stack)
