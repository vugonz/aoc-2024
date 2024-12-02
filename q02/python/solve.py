import os
from typing import Optional, Tuple

INPUT_TXT = os.path.join(os.path.dirname(__file__), "../input.txt")


def analyse_array(start: int, arr: list[int]) -> Tuple[bool, Optional[Tuple[int, int]]]:
    ascending = int(arr[start]) < int(arr[start + 1])
    for i in range(start + 1, len(arr)):
        current = int(arr[i])
        prev = int(arr[i - 1])
        if abs(current - prev) < 1 or abs(current - prev) > 3:
            return False, (i, i - 1)
        if ascending and (current < prev):
            return False, (i, i - 1, i - 2)
        if not ascending and (current > prev):
            return False, (i, i - 1, i - 2)

    return True, None


def part_one() -> int:
    data = open(INPUT_TXT, "r").read().splitlines()

    safe = 0
    for line in data:
        arr = line.split(" ")
        valid, _ = analyse_array(0, arr)
        if valid:
            safe += 1
    return safe


def part_two() -> int:
    data = open(INPUT_TXT, "r").read().splitlines()

    safe = 0
    for line in data:
        arr = line.split(" ")
        valid, lvl_idxs = analyse_array(0, arr)
        if valid:
            safe += 1
            continue

        for i in lvl_idxs:
            if i < 0:
                continue
            valid, _ = analyse_array(i - 2 if i - 2 > 0 else 0, arr[:i] + arr[i + 1 :])
            if valid:
                safe += 1
                break
    return safe


if __name__ == "__main__":
    data = open(INPUT_TXT, "r").read().splitlines()
    print(part_one(), part_two())
