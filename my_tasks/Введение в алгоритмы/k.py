def main():
    n = int(input())
    digits = ''.join(input().split())
    k = int(input())
    result = str((int(digits) + k))
    for i in result:
        print(i, end=' ')

if __name__ == '__main__':
    main()