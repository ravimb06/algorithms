def main():
    inputed_text = input().lower()
    reg = re.compile('[^a-zA-Z]')
    text = reg.sub('', inputed_text)
    reversed_text = text[::-1]
    is_palindrome = True
    for i in range(len(text)):
        if text[i] != reversed_text[i]:
            is_palindrome = False
            break
    print(is_palindrome)

if __name__ == '__main__':
    main()
