def isValid(s: str) -> bool:
    ret = False

    my_stack = 0

    for x in s:
        print(x, end='')

        if x == '(' or x == '{' or x == '[':
            my_stack += 1
        elif x == ')' or x == '}' or x == ']':
            my_stack -= 1
        else:
            pass

    return my_stack == 0


if __name__ == "__main__":
    line = "jkgljdfkslgfds()"

    if isValid(line):
        print("Valid")
    else:
        print("invalid")
