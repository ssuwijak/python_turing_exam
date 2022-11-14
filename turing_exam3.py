from typing import List


def solution(morsecode: str) -> List[str]:
    morsecode = morsecode.strip()
    morse_len = len(morsecode)

    ans = []

    print("== original word is ==\n{}\n".format(morsecode))

    findword = ".."
    replaceby = "--"
    replaceby_len = len(replaceby)

    i_max = 500-replaceby_len
    i = 0
    while i < morse_len and i < i_max:
        i = morsecode.find(findword, i)
        if i > -1:
            value = morsecode[:i] + replaceby + morsecode[i+2:]
            ans.append(value)

            i += 1
            print(value)
        else:
            break

    # print(ans)

    return ans


if __name__ == "__main__":
    line = "1.2..3...4....5.....6......7..."
    solution(line)
    # print(solution(line))
