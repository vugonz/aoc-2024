data = None


def solve1():
    first, second = [], []
    for line in data:
        f, s = line.split("   ")
        first.append(int(f))
        second.append(int(s))

    first.sort()
    second.sort()

    r = 0
    for i, val in enumerate(first, 0):
        r += abs(val - second[i])

    return r


def solve2():
    first, second = [], []
    for line in data:
        f, s = line.split("   ")
        first.append(int(f))
        second.append(int(s))

    occurs = {}
    for item in second:
        if occurs.get(item, 0) == 0:
            occurs[item] = 0
        occurs[item] += 1

    r = 0
    for item in first:
        r += item * occurs.get(item, 0)

    return r


if __name__ == "__main__":
    data = open("/home/vugz/aoc/1/input.txt", "r").read().splitlines()
    print(solve1())
    print(solve2())
