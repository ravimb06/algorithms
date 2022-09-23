def main():
    amount_days = int(input())
    temperatures = list(map(int, input().split()))
    counter = 0
    if amount_days > 1:
        for i in range(len(temperatures)):
            if i > 0 and i < len(temperatures) - 1:
                if temperatures[i] > temperatures[i-1] and temperatures[i] > temperatures[i+1]:
                    counter += 1
            if i == 0 and temperatures[i] > temperatures[i+1]:
                counter += 1
            if i == len(temperatures) - 1 and temperatures[i] > temperatures[i-1]:
                counter += 1
    if amount_days == 1:
        counter += 1
    print(counter)

if __name__ == '__main__':
    main()
