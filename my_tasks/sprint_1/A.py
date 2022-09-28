import sys


def main():
    n = int(input())
    digits = sys.stdin.readline().rstrip().split()
    n_distance = []
    for i in range(n):
        dist_1 = False
        dist_2 = False
        if int(digits[i]) == 0:
            n_distance.append(0)
        else:
            for j in range(i):
                if int(digits[j]) == 0:
                    dist_1 = j
                    print('cikl', i, j, dist_1)
            for k in range(i, n):
                if int(digits[k]) == 0:
                    dist_2 = k
                    print('cikl', i, k, dist_2)
                    break
            if dist_1 > -1 and not dist_2:
                n_distance.append(i - dist_1)
                print('cikla', i, i - dist_1)
            elif dist_2 and dist_1 < 0:
                n_distance.append(dist_2 - i)
                print('ciklb', i, dist_2 - i)
            else:
                if (i - dist_1) <= (dist_2 - i):
                    n_distance.append(i - dist_1)
                    print('ciklc', i, i - dist_1)
                if (dist_2 - i) <= (i - dist_1):
                    n_distance.append(dist_2 - i)
                    print('cikld', i, dist_2 - i)
    print(n_distance)


if __name__ == '__main__':
    main()
