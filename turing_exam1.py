def calPoint(ops) -> int:
    scores = []
    sum = 0

    log("0) initilize")

    for idx, x in enumerate(ops):

        x = x.upper().strip()
        score_count = len(scores)

        flagSkip = True

        if int_tryparse(x):  # x.isdigit():
            flagSkip = False
            scores.append(int(x))
            log(f"{idx+1}) add {x} .. {scores}")
        elif x == '+':
            if score_count >= 2:
                flagSkip = False
                sum = int(scores[-1])+int(scores[-2])
                scores.append(sum)

                log(f"{idx+1}) add sum of last 2 scores .. {scores}")
        elif x == 'D':
            if score_count >= 1:
                flagSkip = False
                sum = int(scores[-1]) * 2
                scores.append(sum)
                log(f"{idx+1}) add double of last score .. {scores}")
        elif x == 'C':
            if score_count >= 1:
                flagSkip = False
                scores.pop(score_count-1)
                log(f"{idx+1}) remove last score .. {scores}")
        else:
            pass

        if flagSkip:
            log(f"{idx+1}) ignore and skip for '{x}'")
    sum = 0
    for x in scores:
        sum += int(x)

    log(f"\nraw score is {ops}", True)
    log(f"total score of {scores} is {sum}", True)

    return sum


def int_tryparse(value):
    ret = False
    try:
        i = int(value)
        ret = True
    except:
        i = -1

    return ret


def log(msg, debugMode=True):
    if debugMode:
        print(msg)


if __name__ == "__main__":
    line = "+ 5 -2 4 zz c d 9 + +"
    ops = line.strip().split()
    calPoint(ops)
    # print(calPoint(ops))
