def main():
    digit = int(input())
    degrees = 4
    result = 'False'
    if digit == 1:
        print('True')
    elif digit % 2 != 0:
        print(result)
    else:
        while digit >= degrees:
            if degrees == digit:
                result = 'True'
            degrees = degrees * 4
        print(result)

if __name__ == '__main__':
    main()