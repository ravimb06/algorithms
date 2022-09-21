import sys

def main():
    digits = sys.stdin.readline().rstrip().split()
    even = False
    odd = False
    for i in digits:
        if int(i) % 2 == 0:
            even = True
        else:
            odd = True
    if even == True and odd == True:
        print('FAIL')
    else:
        print('WIN')

if __name__ == '__main__':
    main()
