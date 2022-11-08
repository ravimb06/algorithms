# 74179546

def quicksort(arr, left, right):
    if right <= left:
        return
    left_idx = left
    right_idx = right
    pivot = arr[(left + right)//2]
    while left_idx < right_idx:
        while arr[left_idx] < pivot:
            left_idx += 1
        while arr[right_idx] > pivot:
            right_idx -= 1
        if left_idx <= right_idx:
            arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]
            left_idx += 1
            right_idx -= 1
    quicksort(arr, left, right_idx)
    quicksort(arr, left_idx, right)


if __name__ == '__main__':
    participants_amount = int(input())
    list_of_competitors = [None] * participants_amount
    for i in range(participants_amount):
        name, tasks, mistakes = input().split()
        list_of_competitors[i] = (-int(tasks), int(mistakes), name)

    quicksort(list_of_competitors, 0, len(list_of_competitors)-1)
    print(*[i[2] for i in list_of_competitors], sep='\n')
