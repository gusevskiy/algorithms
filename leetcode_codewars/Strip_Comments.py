'''
Завершите решение так, чтобы оно удаляло весь текст,
следующий за любым из переданных маркеров комментариев. Все пробелы
в конце строки также должны быть удалены.
'''

# Мое решение (я делал на очистке и соединение)
def strip_comments(strng, markers):
    res = []
    for i in strng.split('\n'):
        x = [y for y in markers if y in i]
        if x:
            index = i.find(*x)
            res.append(i[:index].rstrip())
        else:
            res.append(i.rstrip())
    return '\n'.join(res)


# нужно было делать (удалять на полной строке разделенной через \n)
def solution(string, markers):
    ss = string.split('\n')
    for i in range(len(ss)):
        s = ss[i]
        for marker in markers:
            index = s.find(marker)
            if index >= 0:
                s = s[:index].rstrip()
        ss[i] = s
    return '\n'.join(ss)


if __name__ == '__main__':
    s = "apples, pears # and bananas\ngrapes\nbananas !apples"
    # print(strip_comments(s, ["#", "!"]))
    print(solution(s, ["#", "!"]))
