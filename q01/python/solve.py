import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), "../input.txt")


def part_one() -> int:
    data = open(INPUT_TXT, "r").read().splitlines()

    left, right = [], []
    for line in data:
        f, s = line.split("   ")
        left.append(int(f))
        right.append(int(s))
    left.sort()
    right.sort()

    r = 0
    for i, val in enumerate(left, 0):
        r += abs(val - right[i])
    return r


def part_two() -> int:
    data = open(INPUT_TXT, "r").read().splitlines()

    left, right = [], []
    for line in data:
        f, s = line.split("   ")
        left.append(int(f))
        right.append(int(s))

    occurs = {}
    for item in left:
        if occurs.get(item, 0) == 0:
            occurs[item] = 0
        occurs[item] += 1

    r = 0
    for item in right:
        r += item * occurs.get(item, 0)
    return r


if __name__ == "__main__":
    print(part_one(), part_two())
