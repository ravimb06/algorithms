def main():
    digit_1 = input()
    digit_2 = input()

    def to_decimal(digit):
        decimal = 0
        degrees = []
        for i in range(len(digit)-1, -1, -1):
            degrees.append(i)
        for i in range(len(digit)):
            decimal += int(digit[i]) * 2 ** degrees[i]
        return decimal

    def to_binary(digit):
        binary = ''
        if digit < 2:
            print(digit)
        else:
            while digit > 0:
                binary += str(digit % 2)
                digit = digit // 2
        return binary[::-1]
    
    sum_digits = to_decimal(digit_1) + to_decimal(digit_2)
    print(to_binary(sum_digits))

if __name__ == '__main__':
    main()
