import os
from itertools import pairwise

INPUT_TXT = os.path.join(os.path.dirname(__file__), "../input.txt")


def part_one() -> int:
    data = open(INPUT_TXT, "r").read().splitlines()
    # add padding
    data = list(map(lambda x: "0" + x + "0", data))
    data = ["0" * len(data[0])] + data
    data += ["0" * len(data[0])]

    def check_neighbors(i, j: int) -> int:
        # fmt: off
        offsets = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        )
        # fmt: on

        r = 0
        for di, dj in offsets:
            n_i, n_j = i + di, j + dj
            count = 0
            for c in "MAS":
                if c != data[n_i][n_j]:
                    break
                count += 1
                n_i += di
                n_j += dj
            if count == 3:
                r += 1
        return r

    def check_diagonal(i, j: int) -> int:
        # fmt: off
        offsets = [(-1, -1), (-1, +1), (+1, +1), (+1, -1)]
        n = tuple(pairwise(offsets + [offsets[0],]))
        # fmt: on
        r = 0
        # Four possibilities
        # M . M   |  S . M  |  S . S  |  M . S
        # . A .   |  . A .  |  . A .  |  . A .
        # S . S   |  S . M  |  M . M  |  M . S
        # TODO I lost the code that works, will be added soon

        return r

    r1 = 0
    r2 = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] == "X":
                r1 += check_neighbors(i, j)
            elif data[i][j] == "A":
                r2 += check_diagonal(i, j)

    return r1, r2


if __name__ == "__main__":
    print(part_one())
