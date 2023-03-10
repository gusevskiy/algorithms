def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    long = []
    for i in line.split(' '):
        if len(i) > len(long):
            long = i
    return long


if __name__ == '__main__':
    a = 'i love segment tree'
    print(get_longest_word(a))

