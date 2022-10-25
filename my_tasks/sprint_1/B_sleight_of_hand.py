# 73037834

def get_neighbors(to_press: int, numbers: str) -> int:
    record = sum([int(value)//int(value) for value in set(numbers) if numbers.count(value) <= to_press])
    return record


def read_input():
    to_press = int(input()) * 2
    matrix = []
    for _ in range(4):
        matrix.append(input().replace('.', ''))
    numbers = ''.join(matrix)
    return to_press, numbers


if __name__ == "__main__":
    to_press, numbers = read_input()
    print(get_neighbors(to_press, numbers))
