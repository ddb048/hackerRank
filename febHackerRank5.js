##NOTE - plus one

##NOTE - given a large integer

function plus_one(digits) {
    let string = digits.join("")

    let num = parseInt(string)

    let resNum = num + 1

    let stringRes = resNum.toString()

    let res = stringRes.split("")

    return res

}

def plus_one(digits: list[int]) -> list[int]:
    # Write your code here
rev = digits[:: -1]
one, i = 1, 0
while one:
    if i < len(rev):
        if rev[i] == 9:
            rev[i] = 0
        else:
        rev[i] += 1
one = 0
            else:
rev.append(1)
one = 0
i += 1
return rev[:: -1]
