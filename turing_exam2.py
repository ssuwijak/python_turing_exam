def isValid(s: str) -> bool:
    brackets = [0, 0, 0]
    sum_stack = 0

    for x in s:
        log(x, True, False)

        if x == '(':
            brackets[0] += 1
        elif x == '{':
            brackets[1] += 1
        elif x == '[':
            brackets[2] += 1
        elif x == ')':
            if brackets[0] < 1:
                log("\n() closing out of order")
                brackets[0] -= 1
            brackets[0] -= 1
        elif x == '}':
            if brackets[1] < 1:
                log("\n{} closing out of order")
                brackets[1] -= 1
            brackets[1] -= 1
        elif x == ']':
            if brackets[2] < 1:
                log("\n[] closing out of order")
                brackets[2] -= 1
            brackets[2] -= 1
        else:
            pass

    if brackets[0] != 0:
        log("\nfinally () not be closed completely")
    elif brackets[1] != 0:
        log("\nfinally {} not be closed completely")
    elif brackets[2] != 0:
        log("\nfinally [] not be closed completely")
    else:
        pass

    sum_stack = brackets[0]+brackets[1]+brackets[2]

    return sum_stack == 0


def log(msg, debugMode=True, newline=True):
    if debugMode:
        if newline:
            print(msg)
        else:
            print(msg, end='')


if __name__ == "__main__":
    line = "jkgljdfkslgfds]([)"

    if isValid(line):
        print("Valid")
    else:
        print("invalid")
