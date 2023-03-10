def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    line = ''.join(c for c in line if c.isalpha()).lower()
    if line == line[::-1]:
        return True
    return False



if __name__ == '__main__':
    a = 'A man, a plan, a canal: Panama'

    print(is_palindrome(a))