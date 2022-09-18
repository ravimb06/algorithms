from typing import List, Tuple, Optional

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    previous = set()
    for A in arr:
        Y = target_sum - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)
    return None

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))