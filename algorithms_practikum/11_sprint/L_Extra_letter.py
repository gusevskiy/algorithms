str_1 = 'go'
str_2 = 'ogg'


def get_excessive_letter(shorter: str, longer: str) -> str:
    # Здесь реализация вашего решения
    tmp = list(longer)
    for c in shorter:
        if c in longer:
            tmp.remove(c)
    return ''.join(tmp)


if __name__ == '__main__':
    print(get_excessive_letter(str_1, str_2))