# 73036869
from typing import List


def get_dist(houses_list: List[int]) -> List[int]:
    last_zero = houses_list.index(0)

    for index, house in enumerate(houses_list):
        if house == 0:
            last_zero = index
        else:
            houses_list[index] = abs(index - last_zero)

    houses_list = houses_list[::-1]
    last_zero = houses_list.index(0)

    for index, house in enumerate(houses_list):
        if house == 0:
            last_zero = index
        else:
            houses_list[index] = min(abs(index - last_zero), house)

    return houses_list[::-1]


def read_input():
    input()
    houses_list = [int(x) for x in input().strip().split()]
    return houses_list


if __name__ == "__main__":
    houses_list = read_input()
    print(' '.join(map(str, get_dist(houses_list))))
