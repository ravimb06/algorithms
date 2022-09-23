def main():
    len_text = int(input())
    text = list(input().split())
    max_word = text[0]
    for i in range(len(text)):
        if len(text[i]) > len(max_word):
            max_word = text[i]
    print(max_word)
    print(len(max_word))

if __name__ == '__main__':
    main()
