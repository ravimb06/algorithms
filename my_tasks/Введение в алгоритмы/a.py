import sys

def main():
    digits = sys.stdin.readline().rstrip().split()
    a = int(digits[0])
    x = int(digits[1])
    b = int(digits[2])
    c = int(digits[3])
    y = a * x ** 2 + b * x + c
    print(y)

if __name__ == '__main__':
    main()
