import os
import itertools
from functools import wraps

INPUT_TXT = os.path.join(os.path.dirname(__file__), "../input.txt")


def cache_arr(f):
    arr = [0] * 16

    @wraps(f)
    def wrapper(size):
        nonlocal arr
        if not arr[size]:
            arr[size] = f(size)
        return arr[size]

    return wrapper


@cache_arr
def operations_positions(size: int):
    return tuple(itertools.product([0, 1, 2], repeat=size - 1))


def is_valid_operation(r: int, *args) -> bool:
    for c in operations_positions(len(args)):
        check = int(args[0])
        for i, n in enumerate(args[1:], 1):
            if c[i - 1] == 0:
                check += int(n)
            elif c[i - 1] == 1:
                check *= int(n)
            else:
                check = int(str(check) + str(int(n)))

        if check == r:
            return True

    return False


def solve() -> int:
    data = open(INPUT_TXT, "r").read().splitlines()

    r = 0
    for line in data:
        lh, rh = line.split(":")
        args = rh.split(" ")[1:]
        if is_valid_operation(int(lh), *args):
            r += int(lh)

    return r


if __name__ == "__main__":
    print(solve())
