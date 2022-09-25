def main():
    s = input()
    t = input()
    for i in t:
        if t.count(i) != s.count(i):
            print(i)
            break

if __name__ == '__main__':
    main()
