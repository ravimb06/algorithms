def bubble_sort(number, source_array):
    flag = 1
    for i in range(number - 1):
        for j in range(0, number-i-1):
            if source_array[j] > source_array[j+1]:
                source_array[j], source_array[j+1] = (source_array[j+1],
                                                      source_array[j])
                flag = 1
        if flag == 1:
            for x in source_array:
                print(x, end=' ')
            print('')
            flag = 0


if __name__ == '__main__':
    number = int(input())
    source_array = [int(num) for num in input().split(' ')]
    bubble_sort(number, source_array)
