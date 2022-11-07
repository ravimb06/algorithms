def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if int(arr[0]) >= x:
        return 1
    elif int(arr[mid]) >= x and x > int(arr[mid-1]):
        return mid + 1
    elif x <= int(arr[mid]):
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


amount_days = int(input())
money_sum = input().split()
bike_cost = int(input())
one_bike = binarySearch(money_sum, bike_cost, 0, amount_days)
two_bikes = binarySearch(money_sum, bike_cost * 2, one_bike, amount_days)
print(one_bike, two_bikes)
