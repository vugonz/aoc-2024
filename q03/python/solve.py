import os
from typing import Tuple

INPUT_TXT = os.path.join(os.path.dirname(__file__), "../input.txt")


def solve(second: bool = False) -> int:
    data = open(INPUT_TXT, "r").read()

    def check_num(i) -> Tuple[int, int]:
        """Matches num in expression. 0 if no number in expression"""
        j = i
        n = 0
        while (c := data[j]).isnumeric():
            n = n * 10 + int(c)
            j += 1

        return n, j

    def check_keyword(keyword, i) -> Tuple[bool, int]:
        """Matches keyword in expression. False if it fails"""
        if i + len(keyword) > len(data):
            raise EOFError

        return (
            (True, i + len(keyword))
            if data[i : i + len(keyword)] == keyword
            else (False, i)
        )

    def match_mul_expr(i) -> int:
        while True:
            i = toggle(i)
            valid, i = check_keyword("mul(", i)
            if not valid:
                i += 1
                continue
            n1, i = check_num(i)
            if n1 == 0:
                continue
            valid, i = check_keyword(",", i)
            if not valid:
                continue
            n2, i = check_num(i)
            if n2 == 0:
                continue
            valid, i = check_keyword(")", i)
            if not valid:
                continue
            return n1, n2, i

    def toggle(i: int) -> int:
        nonlocal enabled
        valid, i = check_keyword("don't()" if enabled else "do()", i)
        if valid:
            enabled = not enabled
        return i

    if not second:
        toggle = lambda x: x  # noqa: E731

    r = 0
    i = 0
    enabled = True
    try:
        while True:
            n1, n2, i = match_mul_expr(i)
            if enabled:
                r += n1 * n2
    except EOFError:
        pass

    return r


if __name__ == "__main__":
    print(solve(), solve(second=True))
