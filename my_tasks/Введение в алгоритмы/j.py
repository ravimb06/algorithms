def main():
    n = int(input())
    multipliers = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            multipliers.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        multipliers.append(n)
    for i in multipliers:
        print(i, end=' ')

if __name__ == '__main__':
    main()