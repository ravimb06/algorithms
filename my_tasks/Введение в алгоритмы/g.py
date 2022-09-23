def main():
    digit = int(input())
    binary = ''
    if digit < 2:
        print(digit)
    else:
        while digit > 0:
            binary += str(digit % 2)
            digit = digit // 2
    print(binary[::-1])

if __name__ == '__main__':
    main()
