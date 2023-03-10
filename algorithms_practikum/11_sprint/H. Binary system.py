def get_sum(first_number: str, second_number: str) -> str:
    # Здесь реализация вашего решения
    first_number = list(first_number[::-1])
    second_number = list(second_number[::-1])
    first_number = list(map(int, first_number))
    second_number = list(map(int, second_number))
    max_size = max(len(first_number), len(second_number))
    first_number += [0] * (max_size - len(first_number))
    second_number += [0] * (max_size - len(second_number))
    overflow = 0
    result = []
    for obj in zip(first_number, second_number):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        result.append(value % 2)
    if overflow == 1:
        result.append(1)
    result = result[::-1]
    return ''.join(map(str, result))


if __name__ == '__main__':
    print(get_sum('1010', '1011'))
    # a = (list(zip('1010', '1011')))
    # print(list(a[::-1]))
    # print(int(a[::-1][0][1]) + int(a[::-1][0][1]))
