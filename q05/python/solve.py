from typing import Optional, Tuple
import os
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), "../input.txt")


def is_valid_page(rules, page) -> Tuple[bool, Optional[Tuple[int, int]]]:
    for i, c in enumerate(page, 0):
        for j, c2 in enumerate(page[i + 1 :], 0):
            if c2 not in rules[c][1]:
                return False, i, j + i + 1
    return True, 0, 0


def part_one() -> int:
    data: list = open(INPUT_TXT, "r").read().splitlines()
    i = data.index("")
    rules = data[:i]
    pages = data[i + 1 :]

    rules_map: dict[str] = defaultdict(list)
    for rule in rules:
        a, b = rule.split("|")
        if len(rules_map[a]) == 0:
            rules_map[a].append(set())
            rules_map[a].append(set())
        if len(rules_map[b]) == 0:
            rules_map[b].append(set())
            rules_map[b].append(set())

        rules_map[a][1].add(b)
        rules_map[b][0].add(a)

    r = 0
    for raw_page in pages:
        page = raw_page.split(",")

        valid, i, j = is_valid_page(rules_map, page)
        if valid:
            continue

        while not valid:
            page[i], page[j] = page[j], page[i]
            valid, i, j = is_valid_page(rules_map, page)
        r += int(page[len(page) // 2])

    return r


if __name__ == "__main__":
    print(part_one())
